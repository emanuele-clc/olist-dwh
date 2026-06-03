# L3 - Cleaning: orders

**Data:** 2026-05-09 11:50 | **Provider:** ollama

## Piano di Cleaning

```json
{
  "table": "orders",
  "steps": [
    {
      "step_id": 1,
      "name": "Elimina righe con dati mancanti",
      "description": "Rimuovere le righe con valori null per i colonni 'order_approved_at', 'order_delivered_carrier_date' e 'order_delivered_customer_date'.",
      "columns": ["order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date"],
      "pandas_method": "dropna",
      "priority": "high",
      "business_impact": "Rimozione dati non pertinenti per ottimizzare le query"
    },
    {
      "step_id": 2,
      "name": "Converte tipi di dati",
      "description": "Convertire i valori dei colonni 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date' e 'order_delivered_customer_date' da stringa a datetime.",
      "columns": ["order_purchase_timestamp", "order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date"],
      "pandas_method": "to_datetime",
      "priority": "high",
      "business_impact": "Conversione dei tipi di dati per semplificare le date"
    },
    {
      "step_id": 3,
      "name": "Elimina righe con valori duplicati",
      "description": "Rimuovere le righe duplicate.",
      "columns": [],
      "pandas_method": "drop_duplicates",
      "priority": "medium",
      "business_impact": "Rimozione dati non pertinenti per ridurre la dimensione del set di dati"
    },
    {
      "step_id": 4,
      "name": "Ordina le righe per ordine di acquisizione",
      "description": "Organizzare le righe in base all'ordine di acquisto.",
      "columns": ["order_purchase_timestamp"],
      "pandas_method": "sort_values",
      "priority": "low",
      "business_impact": "Ordinamento delle righe per facilità di consultazione"
    }
  ]
}
```

## Narrativa Audit

**Audit Qualità Dati su Tabella "orders"**

**Introduzione**

Il presente audit ha avuto lo scopo di valutare la qualità dei dati contenuti nella tabella "orders" del database DW e-commerce. Il processo di analisi è stato condotto con un ciclo completo di deduplicazione, standardizzazione, data parsing, imputation e feature engineering.

**Intervento e Trasformazioni Principali**

Il ciclo di elaborazione ha comportato le seguenti trasformazioni principali:

1.  **Deduplication**: sono stati rimossi 0 duplicati dalla tabella "orders".
2.  **Standardizzazione**: è stata eseguita la standardizzazione delle colonne "order_status" tramite la funzione `strip + lower`.
3.  **Data Parsing**: sono state convertite 5 colonne datetime nella tabella "orders" in un formato coerente.
4.  **Imputation**: sono state imparate le date mancanti con una flag binaria (mancanza = informazione).
5.  **Feature Engineering**: sono stati aggiunti 4 nuovi campi: `_approved_missing`, `_delivered_carrier_missing`, `_delivered_customer_missing` e `delivery_lead_days`, `delivery_delay_days`, `purchase_year` e `purchase_month`.

**Impatto Qualità**

Il ciclo di elaborazione ha avuto un impatto significativo sulla qualità dei dati della tabella "orders". È stato possibile:

*   Rimuovere duplicati non rilevanti.
*   Standardizzare le colonne per facilitare la comprensione e l'analisi dei dati.
*   Convertire le date mancanti in un formato coerente.
*   Aggiungere nuovi campi utili per lo studio dei dati.

**Limitazioni**

Il processo di elaborazione non ha avuto alcuna limitazione significativa, tuttavia è stato necessario:

*   Verificare la presenza di duplicati e mancanti prima dell'elaborazione.
*   Controllare le funzioni standardizzanti e data parsing per assicurarsi che si tratti di un comportamento coerente.

**Raccomandazioni**

Per migliorare ulteriormente la qualità dei dati della tabella "orders":

*   Verificare regolarmente l'elaborazione degli dati per garantire la precisione e la consistenza.
*   Considerare l'utilizzo di funzioni standardizzanti più avanzate o di tecniche di data quality come il test degli indici numerici.
*   Utilizzare strumenti di analisi di qualità dei dati per monitorare costantemente le prestazioni della tabella.
