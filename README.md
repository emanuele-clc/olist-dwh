# Olist Data Warehouse — Setup

## Requisiti

- Python 3.9+
- Jupyter Notebook o JupyterLab
- Librerie: `pandas`, `numpy`, `sqlite3` (incluso in Python), `matplotlib`, `seaborn`

Installa tutto con:
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

---

## Setup su un nuovo PC

### 1. Clona la repository
```bash
git clone https://github.com/emanuele-clc/olist-dwh.git
cd olist-dwh
```

### 2. Scarica i raw data da Kaggle
Vai su: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Scarica il dataset e metti i seguenti file nella cartella `1_raw_data/`:

```
olist_customers_dataset.csv
olist_geolocation_dataset.csv
olist_order_items_dataset.csv
olist_order_payments_dataset.csv
olist_order_reviews_dataset.csv
olist_orders_dataset.csv
olist_products_dataset.csv
olist_sellers_dataset.csv
product_category_name_translation.csv
```

> Il file `olist_geolocation_dataset.csv` è escluso dalla repo perché pesa 58MB.

### 3. Esegui il notebook principale
```bash
jupyter notebook 2_scripts/olist_dw_cleaning_pipeline.ipynb
```

Esegui tutte le celle in ordine. Il notebook:
- Pulisce i dati grezzi
- Costruisce il database SQLite (`6_database/olist_dw.db`)
- Esporta i CSV del Data Warehouse in `9_exported_from_db/`

### 4. Apri Tableau
- Apri `8_tableau/Cartella1.twb`
- Se Tableau chiede di ricollegare i dati, punta alla cartella `9_exported_from_db/`

---

## Struttura della cartella

```
consegna/
├── 1_raw_data/          # Dataset originali Olist (da Kaggle)
├── 2_scripts/           # Notebook ETL e cleaning pipeline
├── 6_database/          # Database SQLite generato (non in repo)
├── 7_report/            # Relazione LaTeX + PDF
├── 8_tableau/           # Visualizzazioni Tableau (.twb)
├── 9_exported_from_db/  # CSV del DWH esportati dal DB
└── README.md
```

---

## Note

- Il database `olist_dw.db` non è incluso nella repo perché supera i 100MB. Viene generato eseguendo il notebook.
- La story Tableau è già configurata e si collega automaticamente ai CSV in `9_exported_from_db/`.
