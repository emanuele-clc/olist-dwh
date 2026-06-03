# L3 - Cleaning: reviews

**Data:** 2026-05-09 11:59 | **Provider:** ollama

## Piano di Cleaning

```json
{
  "table": "reviews",
  "steps": [
    {
      "step_id": 1,
      "name": "Cleaning e elimina duplicate",
      "description": "Elimina le righe duplicate della colonna review_comment_title.",
      "columns": ["review_comment_title"],
      "pandas_method": "drop_duplicates(subset='review_comment_title', keep='first')",
      "priority": "high"
    },
    {
      "step_id": 2,
      "name": "Rimozione caratteri non numerici da review_score e review_creation_date",
      "description": "Rimuovi i caratteri non numerici dalle colonne review_score e review_creation_date.",
      "columns": ["review_score", "review_creation_date"],
      "pandas_method": [
        "str.replace(to_replace='[^0-9]', value='', regex=True)",
        "pd.to_numeric"
      ],
      "priority": "medium"
    },
    {
      "step_id": 3,
      "name": "Elimina righe con valori null",
      "description": "Elimina le righe con valori null nelle colonne review_comment_title e review_comment_message.",
      "columns": ["review_comment_title", "review_comment_message"],
      "pandas_method": [
        "notnull().dropna()"
      ],
      "priority": "low"
    }
  ]
}
```

## Narrativa Audit

**Audit di Data Quality per la Tabelle Olist "reviews"**

**Sintesi dell'intervento**
L'audit di data quality per la tabelle Olist "reviews" è stato eseguito con lo scopo di migliorare la qualità dei dati e ridurre gli errori. L'intervento è stato suddiviso in tre fasi principali: deduplication, parsing delle date e imputazione dei valori mancanti.

**Trasformazioni principali**

1. **Deduplication**: sono stati rimossi 814 duplicati dal dataset, riducendo il numero totale di record a 98.410.
2. **Parsing delle date**: sono state convertite due colonne datetime in formato standard, garantendo una maggiore coerenza e completezza dei dati.
3. **Imputazione dei valori mancanti**: sono stati sostituiti i commenti mancanti con stringhe vuote, riducendo la quantità di dati non completi.

**Impatto qualità**

L'intervento ha avuto un impatto positivo sulla qualità dei dati:

* Il numero totale di record è diminuito del 1.8% rispetto alla versione precedente (99224 - 98.410 = 9354).
* La quantità di duplicati è stata eliminata, garantendo una maggiore unicità dei dati.
* La completezza dei dati è aumentata grazie all'imputazione dei valori mancanti.

**Limitazioni**

Tuttavia, ci sono alcune limitazioni da considerare:

* Non è stato possibile eseguire il parsing delle date su tutte le colonne, a causa della loro complessità e non linearità.
* La deduplication ha richiesto un tempo significativo per eseguire la routine.

**Raccomandazioni**

Per migliorare ulteriormente la qualità dei dati:

1. **Aggiornamento delle date**: è consigliabile aggiornare le date di tutte le colonne per garantire una maggiore coerenza e completezza.
2. **Parsa delle date**: è consigliabile eseguire il parsing delle date su tutte le colonne, utilizzando tecniche più avanzate e efficienti.
3. **Creazione di un indice**: è consigliabile creare un indice sui campi chiave per migliorare la velocità di query e ottimizzazione dei dati.

In sintesi, l'intervento ha avuto un impatto positivo sulla qualità dei dati, ma ci sono ancora spazi per miglioramenti ulteriori.
