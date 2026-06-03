# Progetto Data Warehouse — Olist Brazilian E-Commerce

**Corso:** Laboratorio di Basi di Dati  
**Studente:** Emanuele Colecchia  
**Anno Accademico:** 2025/2026

---

## Descrizione del progetto

Il progetto riguarda la progettazione e implementazione di un Data Warehouse a partire dal dataset pubblico *Brazilian E-Commerce* di Olist, disponibile su Kaggle. Il lavoro comprende una fase di valutazione della qualità dei dati, una pipeline di cleaning, la costruzione del database in SQLite con architettura a stella, e la realizzazione di analisi OLAP tramite Tableau.

---

## Struttura della repository

```
consegna/
├── 1_raw_data/          # Dataset originali Olist (sorgente: Kaggle)
├── 2_scripts/           # Notebook Jupyter: cleaning pipeline ed ETL
├── 3_cleaned_data/      # CSV risultanti dalla fase di cleaning
├── 4_dq_scorecards/     # Scorecard di Data Quality per ogni tabella
├── 5_dq_plots/          # Grafici di Data Quality (prima e dopo cleaning)
├── 6_database/          # Database SQLite (olist_dw.db)
├── 7_report/            # Relazione tecnica in LaTeX e PDF
├── 8_tableau/           # File Tableau (.twb) con dashboard e story
├── 9_exported_from_db/  # CSV esportati dal DWH (dimensioni e fact table)
├── 10_script_llm/       # Output LLM utilizzati per il DQ Assessment
└── README.md
```

---

## Requisiti tecnici

- Python 3.9+
- Jupyter Notebook
- Librerie Python: `pandas`, `numpy`, `matplotlib`, `seaborn`
- Tableau Desktop (per la visualizzazione)

---

## Riproduzione del progetto

Per riprodurre l'intero progetto su una nuova macchina è sufficiente eseguire il notebook principale in ordine:

```
2_scripts/olist_dw_cleaning_pipeline.ipynb
```

Il notebook esegue automaticamente la pulizia dei dati, la costruzione del database SQLite e l'esportazione dei CSV del Data Warehouse nella cartella `9_exported_from_db/`.

Il file Tableau `8_tableau/Cartella1.twb` è preconfigurato e si collega ai CSV presenti in `9_exported_from_db/`.

---

## Note

- Il dataset originale è disponibile pubblicamente su Kaggle: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- I file di grandi dimensioni (`olist_geolocation_dataset.csv`, `olist_dw.db`) sono gestiti tramite Git LFS.
