Olist Data Warehouse – Emanuele Colecchia (Matricola 276527)
============================================================

STRUTTURA DELLA CONSEGNA
─────────────────────────

1_raw_data/
    Dataset originali scaricati da Kaggle (Brazilian E-Commerce Public Dataset).
    9 file CSV grezzi, non modificati:
      olist_customers_dataset.csv, olist_sellers_dataset.csv,
      olist_products_dataset.csv, olist_geolocation_dataset.csv,
      olist_orders_dataset.csv, olist_order_items_dataset.csv,
      olist_order_payments_dataset.csv, olist_order_reviews_dataset.csv,
      product_category_name_translation.csv

2_scripts/
    olist_dw_cleaning_pipeline.ipynb
        Notebook Jupyter con la pipeline completa di Data Quality + Cleaning.
        Legge da 1_raw_data/, scrive i CSV puliti in 3_cleaned_data/.
    data_quality_assessment_LOCAL.ipynb
        Notebook per il calcolo degli indici DQ e generazione scorecard/grafici.
        Output in 4_dq_scorecards/ e 5_dq_plots/.
    L6_Colab1_OLAP_Insights_Olist.ipynb
        Notebook per analisi OLAP e storytelling sui dati esportati dal DWH.
        Output in 2_scripts/L6_out/.

3_cleaned_data/
    8 CSV puliti generati dalla pipeline di cleaning:
      dim_customers.csv, dim_sellers.csv, dim_products.csv, dim_geolocation.csv
      fact_orders.csv, fact_order_items.csv, fact_payments.csv, fact_reviews.csv
    audit_log.csv → log di ogni operazione di cleaning (tabella, step, righe modificate).

4_dq_scorecards/
    Scorecard CSV per ogni tabella sorgente con i 5 indici di qualità:
    Validity, Completeness, Uniqueness, Consistency, Precision.
    dq_scorecard_ALL.csv → riepilogo aggregato di tutte le tabelle.
    dq_pivot_comparison.csv → confronto prima/dopo cleaning.

5_dq_plots/
    Grafici di Data Quality (heatmap 5 indici per tabella).
    cleaning_pipeline_results.png → risultato visivo del cleaning (IQR outlier flagging).
    dq_comparison_ALL.png → confronto aggregato di qualità prima/dopo.

6_database/
    olist_dw.db → database SQLite con:
      • Reconciled Layer: rec_customers, rec_sellers, rec_products,
        rec_geolocation, rec_orders, rec_order_items, rec_fact_payments,
        rec_fact_reviews
      • Star Schema: dim_date, dim_customer, dim_seller, dim_product,
        dim_payment_type, fact_sales (112.650 righe)
    Aprire con DB Browser for SQLite o qualsiasi SQLite viewer.

7_report/
    relazione_DW_Olist.pdf → relazione completa del progetto.
    relazione_DW_Olist.tex → sorgente LaTeX della relazione.
    Immagini usate nel report: schemi ER, DFM, Star Schema, Attribute Tree,
    grafici DQ, risultati cleaning pipeline.

8_tableau/
    Cartella1.twb → workbook Tableau con dashboard interattiva del DW.
    Connesso ai CSV esportati in 9_exported_from_db/ per compatibilita con Tableau.
    Contiene: analisi vendite, distribuzione geografica, trend temporali,
    performance categorie prodotto e venditori.

9_exported_from_db/
    Tabelle del Data Warehouse esportate come CSV (per uso esterno a SQLite):
      dim_customer_*.csv, dim_date_*.csv, dim_payment_type_*.csv,
      dim_product_*.csv, dim_seller_*.csv, fact_sales_*.csv
    Il suffisso nel nome file indica la data/ora di esportazione.

10_script_llm/
    Tre notebook Jupyter che integrano LLM nel processo di Data Quality:
      L1_LLM_data_quality_assessment.ipynb
          Audit DQ automatico su tutte le 8 tabelle Olist raw.
          Genera: audit tecnico, regole DQ formali, executive summary per tabella.
      L2_Colab2_LLM_Missing_Outliers.ipynb
          Analisi valori mancanti (classificazione MCAR/MAR/MNAR) e outlier
          (metodi IQR e Z-score) su tutte le 8 tabelle.
      L3_Colab2_LLM_Cleaning.ipynb
          Piano di cleaning strutturato JSON e narrativa audit prima/dopo
          per tutte le 8 tabelle.
    documentazione_llm.pdf → documentazione completa dei notebook LLM.
    outputs/ → risultati delle esecuzioni (.md e .json per ogni tabella).

    Configurazione LLM (nella cella di config di ogni notebook):
      LLM_PROVIDER = 'ollama'      # locale, richiede: ollama pull llama3.2:3b
      LLM_PROVIDER = 'openai'      # richiede OPENAI_API_KEY
      LLM_PROVIDER = 'anthropic'   # richiede ANTHROPIC_API_KEY


COME RIESEGUIRE / VERIFICARE IL PROGETTO
────────────────────────────────────
1. Esegui il notebook: 2_scripts/olist_dw_cleaning_pipeline.ipynb
   → genera 3_cleaned_data/ con 8 CSV + audit_log.csv

2. Apri il database finale gia fornito: 6_database/olist_dw.db
   -> contiene Reconciled Layer e Star Schema materializzati.

3. Usa gli export in 9_exported_from_db/ per Tableau oppure apri 8_tableau/Cartella1.twb.

4. (Opzionale) Esegui i notebook LLM in 10_script_llm/
   → genera i report in 10_script_llm/outputs/
