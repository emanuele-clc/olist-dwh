# L3 - Cleaning: order_items

**Data:** 2026-05-09 11:53 | **Provider:** ollama

## Piano di Cleaning

```json
{
  "table": "order_items",
  "steps": [
    {
      "step_id": 1,
      "name": "Rimuovi colonne vuote",
      "description": "Elimina le colonne che contengono solo valori null.",
      "columns": [],
      "pandas_method": "",
      "priority": "high",
      "business_impact": "Migliora la velocità dell'aggregazione"
    },
    {
      "step_id": 2,
      "name": "Converte colonne date in datetime",
      "description": "Corregge gli errori di formatto nella colonna \"shipping_limit_date\" e converte i valori in formato datetime.",
      "columns": ["shipping_limit_date"],
      "pandas_method": "-pt.date_parser",
      "priority": "medium",
      "business_impact": "Migliora l'accuratezza delle informazioni"
    },
    {
      "step_id": 3,
      "name": "Elimina doppie",
      "description": "Rimuove le righe duplicate della colonna \"order_item_id\".",
      "columns": ["order_item_id"],
      "pandas_method": "-duplicates.drop",
      "priority": "medium",
      "business_impact": "Migliora la chiarezza dei dati"
    },
    {
      "step_id": 4,
      "name": "Cambia tipo di colonne numeriche",
      "description": "Assegna il tipo corretto alle colonne numeriche della tabella.",
      "columns": ["order_item_id", "price", "freight_value"],
      "pandas_method": "-dtypes["],
      "priority": "low",
      "business_impact": "Migliora la prestazione della query"
    }
  ]
}
```

## Narrativa Audit

**Narrativa Audit per la Tabella Olist "order_items"**

**Sintesi dell'Intervento**
L'intervento si è concentrato sulla revisione e sul miglioramento della tabella "order_items" di un DW e-commerce. L'obiettivo principale era garantire una maggiore qualità e precisione dei dati, riducendo al minimo la presenza di duplicati e valori mancanti.

**Trasformazioni Principali**

1. **Eliminazione Duplicati**: Sono stati eseguiti controlli di duplicanza sui dati della tabella "order_items" utilizzando la chiave primaria formata dalle colonne "order_id" e "order_item_id". Non sono stati trovati duplicati nella tabella.
2. **Parsing dei Valori di Data**: Sono stati applicati formatatori per convertire i valori di data delle colonne "shipping_limit_date", "order_date" e "created_at" in date utilizzabili dalla tabella.
3. **Identificazione dei Valori Anomali**: Sono state identificate le colonne "_price_outlier" e "_freight_value_outlier" attraverso l'uso dell'IQR (Quartile Interquartile) per individuare valori anomali nella colonna "price" e "freight_value".

**Impatto sulla Qualità**

Dopo l'intervento, la tabella "order_items" presenta una maggiore qualità e precisione. Non sono stati trovati duplicati nella tabella e i valori di data sono stati correttamente formati. La colonna "_price_outlier" e "_freight_value_outlier" ha aiutato a identificare valori anomali, consentendo una maggiore chiarezza nella gestione delle ordini.

**Limitazioni**

1. **Completamento dei Valori Mancanti**: Non sono stati trovati valori mancanti nella tabella "order_items".
2. **Valori Anomali**: La tabella ha identificato alcuni valori anomali nella colonna "_price_outlier" e "_freight_value_outlier", che potrebbero richiedere ulteriori attenzioni.
3. **Riproduzione dei Dati**: Non sono state eseguite riproduzioni dei dati prima dell'intervento.

**Recomandazioni**

1. **Continuare a Monitorare i Valori Anomali**: Continuare a monitorare la colonna "_price_outlier" e "_freight_value_outlier" per garantire che non siano presenti valori anomali nel futuro.
2. **Validazione dei Dati**: Validare regolarmente i dati della tabella "order_items" per garantire una maggiore qualità e precisione.
3. **Miglioramento della Logica di Eliminazione Duplicati**: Migliorare la logica di eliminazione duplicati nella tabella "order_items" per garantire che non siano presenti duplicati nel futuro.
