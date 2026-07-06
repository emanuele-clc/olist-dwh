"""
build_star_schema.py
=====================

Script di ETL che costruisce il layer "data warehouse" (star schema:
dim_date, dim_customer, dim_seller, dim_product, dim_payment_type,
fact_sales) a partire dal "reconciled layer" (tabelle rec_*) generato
dal notebook di cleaning (consegna/2_scripts/olist_dw_cleaning_pipeline.ipynb)
ed esportato come CSV in consegna/3_cleaned_data/.

Riproduce l'architettura ETL (Extract -> Transform -> Load) descritta nella
Sezione 6 della relazione (relazione_DW_Olist.tex):

  - Extract : i CSV puliti vengono caricati nel reconciled layer (rec_*)
              tramite pandas.to_sql(if_exists="replace").
  - Transform: vengono costruite le tabelle dim_* e la fact table fact_sales
              a partire dal reconciled layer (JOIN, aggregazioni, chiavi
              surrogate -- cfr. Sezione 6.2 "Dettaglio dei JOIN").
  - Load    : le tabelle dim_*/fact_sales vengono scritte nel database
              SQLite di output con i vincoli di integrita referenziale
              (PRAGMA foreign_keys = ON).

Regola per il "metodo di pagamento principale" di fact_sales (cfr.
Sezione 4.3 e 6.2 della relazione): per ogni order_id, payment_value e
payment_installments sono la SOMMA su tutte le rate dell'ordine
(indipendentemente dal metodo), mentre payment_type e' quello della
PRIMA rata registrata per l'ordine (first()).

Uso:
    python build_star_schema.py \
        --input-dir ../3_cleaned_data \
        --output-db ../6_database/olist_dw_rebuilt.db

Per impostazione predefinita lo script NON sovrascrive il database di
consegna (olist_dw.db): scrive in olist_dw_rebuilt.db nella stessa
cartella. Per rigenerare olist_dw.db stesso, passare esplicitamente
--output-db olist_dw.db.

Nota di verifica: rieseguendo lo script sui CSV di consegna/3_cleaned_data
si ottiene un fact_sales con lo stesso numero di righe (112.650), gli stessi
date_id e gli stessi payment_type_id di olist_dw.db (verifica riga per riga).
I valori di payment_value differiscono di alcuni centesimi per ~2% delle
righe, in corrispondenza dei pagamenti con _payment_value_outlier = 1: il
database di consegna era stato popolato da una versione precedente della
pipeline di cleaning (con winsorization), poi sostituita con il solo flagging
IQR (cfr. modifiche alla Sezione 3 e al notebook di cleaning). Questo script
riflette quindi la versione corrente della pipeline.
"""

import argparse
import sqlite3
import sys
from pathlib import Path

import pandas as pd


# ---------------------------------------------------------------------------
# Mappatura CSV (consegna/3_cleaned_data) -> tabelle del reconciled layer
# ---------------------------------------------------------------------------
CSV_TO_RECONCILED_TABLE = {
    "dim_customers.csv": "rec_customers",
    "dim_sellers.csv": "rec_sellers",
    "dim_products.csv": "rec_products",
    "dim_geolocation.csv": "rec_geolocation",
    "fact_orders.csv": "rec_orders",
    "fact_order_items.csv": "rec_order_items",
    "fact_payments.csv": "rec_fact_payments",
    "fact_reviews.csv": "rec_fact_reviews",
}

# ---------------------------------------------------------------------------
# DDL del layer "data warehouse" (star schema), come nella Sezione 5 della
# relazione: chiavi surrogate per dim_date/dim_payment_type/fact_sales,
# chiavi naturali per le altre dimensioni, FK su fact_sales.
# ---------------------------------------------------------------------------
DW_LAYER_DDL = """
DROP TABLE IF EXISTS fact_sales;
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS dim_customer;
DROP TABLE IF EXISTS dim_seller;
DROP TABLE IF EXISTS dim_product;
DROP TABLE IF EXISTS dim_payment_type;

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY, date TEXT NOT NULL,
    year INTEGER, quarter INTEGER, month INTEGER, month_name TEXT,
    week INTEGER, day INTEGER, weekday TEXT, is_weekend INTEGER
);

CREATE TABLE dim_customer (
    customer_id TEXT PRIMARY KEY, customer_unique_id TEXT,
    customer_zip_code_prefix INTEGER,
    customer_city TEXT, customer_state TEXT,
    customer_lat REAL, customer_lng REAL
);

CREATE TABLE dim_seller (
    seller_id TEXT PRIMARY KEY, seller_zip_code_prefix INTEGER,
    seller_city TEXT, seller_state TEXT, seller_lat REAL, seller_lng REAL
);

CREATE TABLE dim_product (
    product_id TEXT PRIMARY KEY,
    product_category_name TEXT, product_category_name_english TEXT,
    product_name_lenght REAL, product_description_lenght REAL,
    product_photos_qty REAL, product_weight_g REAL,
    product_length_cm REAL, product_height_cm REAL, product_width_cm REAL
);

CREATE TABLE dim_payment_type (
    payment_type_id INTEGER PRIMARY KEY, payment_type TEXT NOT NULL UNIQUE
);

CREATE TABLE fact_sales (
    sale_id INTEGER PRIMARY KEY,
    order_id TEXT NOT NULL, order_item_id INTEGER NOT NULL,
    product_id TEXT NOT NULL, seller_id TEXT NOT NULL,
    customer_id TEXT NOT NULL, date_id INTEGER NOT NULL,
    payment_type_id INTEGER,
    payment_installments REAL, payment_value REAL,
    price REAL, freight_value REAL, order_status TEXT,
    delivery_lead_days REAL, delivery_delay_days REAL, review_score REAL,
    FOREIGN KEY (date_id)         REFERENCES dim_date(date_id)                ON UPDATE CASCADE,
    FOREIGN KEY (customer_id)     REFERENCES dim_customer(customer_id)         ON UPDATE CASCADE,
    FOREIGN KEY (seller_id)       REFERENCES dim_seller(seller_id)             ON UPDATE CASCADE,
    FOREIGN KEY (product_id)      REFERENCES dim_product(product_id)           ON UPDATE CASCADE,
    FOREIGN KEY (payment_type_id) REFERENCES dim_payment_type(payment_type_id) ON UPDATE CASCADE
);
"""


def load_reconciled_layer(con: sqlite3.Connection, input_dir: Path) -> None:
    """Extract: carica i CSV puliti nel reconciled layer (tabelle rec_*)."""
    for csv_name, table in CSV_TO_RECONCILED_TABLE.items():
        csv_path = input_dir / csv_name
        if not csv_path.exists():
            sys.exit(f"ERRORE: file non trovato: {csv_path}")
        df = pd.read_csv(csv_path)
        df.to_sql(table, con, if_exists="replace", index=False)
        print(f"  - {table:<20s} <- {csv_name:<22s} ({len(df):>6d} righe)")


def build_dim_date(con: sqlite3.Connection) -> None:
    """dim_date: date distinte estratte da order_purchase_timestamp."""
    orders = pd.read_sql(
        "SELECT DISTINCT order_purchase_timestamp FROM rec_orders", con
    )
    ts = pd.to_datetime(orders["order_purchase_timestamp"])
    dates = pd.Series(sorted(ts.dt.date.unique()))

    dt = pd.to_datetime(dates)
    df = pd.DataFrame({
        "date_id": dt.dt.strftime("%Y%m%d").astype(int),
        "date": dt.dt.strftime("%Y-%m-%d"),
        "year": dt.dt.year,
        "quarter": dt.dt.quarter,
        "month": dt.dt.month,
        "month_name": dt.dt.strftime("%B"),
        "week": dt.dt.isocalendar().week.astype(int).values,
        "day": dt.dt.day,
        "weekday": dt.dt.strftime("%A"),
        "is_weekend": dt.dt.dayofweek.isin([5, 6]).astype(int),
    })
    df.to_sql("dim_date", con, if_exists="append", index=False)
    print(f"  - dim_date            ({len(df):>6d} righe)")


def build_dim_payment_type(con: sqlite3.Connection) -> pd.DataFrame:
    """dim_payment_type: valori distinti di payment_type, chiave surrogata
    progressiva nell'ordine di prima occorrenza nei pagamenti riconciliati."""
    payments = pd.read_sql(
        "SELECT payment_type FROM rec_fact_payments", con
    )
    types = payments["payment_type"].drop_duplicates().reset_index(drop=True)
    df = pd.DataFrame({
        "payment_type_id": range(1, len(types) + 1),
        "payment_type": types,
    })
    df.to_sql("dim_payment_type", con, if_exists="append", index=False)
    print(f"  - dim_payment_type    ({len(df):>6d} righe): {list(df['payment_type'])}")
    return df


def build_dim_customer(con: sqlite3.Connection) -> None:
    """dim_customer: clienti riconciliati arricchiti con lat/lng tramite
    LEFT JOIN su rec_geolocation (zip_code_prefix)."""
    customers = pd.read_sql("SELECT * FROM rec_customers", con)
    geo = pd.read_sql(
        "SELECT geolocation_zip_code_prefix AS customer_zip_code_prefix, "
        "geolocation_lat AS customer_lat, geolocation_lng AS customer_lng "
        "FROM rec_geolocation",
        con,
    )
    df = customers.merge(geo, on="customer_zip_code_prefix", how="left")
    df = df[[
        "customer_id", "customer_unique_id", "customer_zip_code_prefix",
        "customer_city", "customer_state", "customer_lat", "customer_lng",
    ]]
    df.to_sql("dim_customer", con, if_exists="append", index=False)
    print(f"  - dim_customer        ({len(df):>6d} righe)")


def build_dim_seller(con: sqlite3.Connection) -> None:
    """dim_seller: venditori riconciliati arricchiti con lat/lng tramite
    LEFT JOIN su rec_geolocation (zip_code_prefix)."""
    sellers = pd.read_sql("SELECT * FROM rec_sellers", con)
    geo = pd.read_sql(
        "SELECT geolocation_zip_code_prefix AS seller_zip_code_prefix, "
        "geolocation_lat AS seller_lat, geolocation_lng AS seller_lng "
        "FROM rec_geolocation",
        con,
    )
    df = sellers.merge(geo, on="seller_zip_code_prefix", how="left")
    df = df[[
        "seller_id", "seller_zip_code_prefix",
        "seller_city", "seller_state", "seller_lat", "seller_lng",
    ]]
    df.to_sql("dim_seller", con, if_exists="append", index=False)
    print(f"  - dim_seller          ({len(df):>6d} righe)")


def build_dim_product(con: sqlite3.Connection) -> None:
    """dim_product: prodotti riconciliati, privati dei flag di qualita
    (_imputed/_outlier), con la traduzione inglese della categoria."""
    df = pd.read_sql(
        "SELECT product_id, product_category_name, "
        "product_category_name_english, product_name_lenght, "
        "product_description_lenght, product_photos_qty, product_weight_g, "
        "product_length_cm, product_height_cm, product_width_cm "
        "FROM rec_products",
        con,
    )
    df.to_sql("dim_product", con, if_exists="append", index=False)
    print(f"  - dim_product         ({len(df):>6d} righe)")


def build_fact_sales(con: sqlite3.Connection, payment_types: pd.DataFrame) -> None:
    """fact_sales: una riga per ogni rec_order_items, con FK verso le
    dimensioni e misure di pagamento/recensione pre-aggregate per ordine."""
    items = pd.read_sql("SELECT * FROM rec_order_items", con)
    orders = pd.read_sql(
        "SELECT order_id, customer_id, order_status, "
        "order_purchase_timestamp, delivery_lead_days, delivery_delay_days "
        "FROM rec_orders",
        con,
    )
    payments = pd.read_sql(
        "SELECT rowid, order_id, payment_sequential, payment_type, "
        "payment_installments, payment_value FROM rec_fact_payments "
        "ORDER BY rowid",
        con,
    )
    reviews = pd.read_sql(
        "SELECT order_id, review_score FROM rec_fact_reviews", con
    )

    # date_id: order_purchase_timestamp -> intero YYYYMMDD
    orders = orders.copy()
    orders["date_id"] = (
        pd.to_datetime(orders["order_purchase_timestamp"])
        .dt.strftime("%Y%m%d")
        .astype(int)
    )

    # LEFT JOIN con i pagamenti pre-aggregati per order_id:
    #   - payment_value, payment_installments: SUM su tutte le rate
    #   - payment_type: first() nell'ordine di caricamento del reconciled
    #     layer (rowid), NON nell'ordine di payment_sequential -- i due
    #     ordini non coincidono per circa meta' degli ordini multi-pagamento.
    pay_agg = payments.groupby("order_id", sort=False, as_index=False).agg(
        payment_type=("payment_type", "first"),
        payment_installments=("payment_installments", "sum"),
        payment_value=("payment_value", "sum"),
    )
    type_to_id = dict(zip(payment_types["payment_type"], payment_types["payment_type_id"]))
    pay_agg["payment_type_id"] = pay_agg["payment_type"].map(type_to_id)

    # LEFT JOIN con le recensioni pre-aggregate (media per ordine)
    rev_agg = reviews.groupby("order_id", as_index=False)["review_score"].mean()

    fact = items.merge(
        orders[["order_id", "customer_id", "order_status", "date_id",
                "delivery_lead_days", "delivery_delay_days"]],
        on="order_id", how="left",
    )
    fact = fact.merge(
        pay_agg[["order_id", "payment_type_id", "payment_installments", "payment_value"]],
        on="order_id", how="left",
    )
    fact = fact.merge(rev_agg, on="order_id", how="left")

    fact = fact.sort_values(["order_id", "order_item_id"]).reset_index(drop=True)
    fact.insert(0, "sale_id", range(1, len(fact) + 1))

    cols = [
        "sale_id", "order_id", "order_item_id", "product_id", "seller_id",
        "customer_id", "date_id", "payment_type_id", "payment_installments",
        "payment_value", "price", "freight_value", "order_status",
        "delivery_lead_days", "delivery_delay_days", "review_score",
    ]
    fact = fact[cols]
    fact.to_sql("fact_sales", con, if_exists="append", index=False)
    print(f"  - fact_sales          ({len(fact):>6d} righe)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-dir", default="../3_cleaned_data",
        help="Cartella con i CSV puliti (default: ../3_cleaned_data)",
    )
    parser.add_argument(
        "--output-db", default="olist_dw_rebuilt.db",
        help="Percorso del database SQLite di output "
             "(default: olist_dw_rebuilt.db, non sovrascrive olist_dw.db)",
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    output_db = Path(args.output_db).resolve()

    print(f"Input (CSV puliti) : {input_dir}")
    print(f"Output (database)  : {output_db}")
    print()

    con = sqlite3.connect(output_db)
    try:
        con.execute("PRAGMA foreign_keys = OFF")  # durante il caricamento

        print("1) EXTRACT - reconciled layer (rec_*)")
        load_reconciled_layer(con, input_dir)

        print("\n2) TRANSFORM - star schema (dim_* + fact_sales)")
        con.executescript(DW_LAYER_DDL)
        build_dim_date(con)
        payment_types = build_dim_payment_type(con)
        build_dim_customer(con)
        build_dim_seller(con)
        build_dim_product(con)
        build_fact_sales(con, payment_types)

        con.execute("PRAGMA foreign_keys = ON")
        con.commit()
        print("\nDatabase scritto correttamente.")
    except Exception as exc:
        con.rollback()
        sys.exit(f"ERRORE durante la build: {exc}")
    finally:
        con.close()


if __name__ == "__main__":
    main()
