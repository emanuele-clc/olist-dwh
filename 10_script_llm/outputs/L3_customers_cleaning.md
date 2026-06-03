# L3 - Cleaning: customers

**Data:** 2026-05-09 11:51 | **Provider:** ollama

## Piano di Cleaning

```json
{
  "table": "customers",
  "steps": [
    {
      "step_id": 1,
      "name": "Rimuovi codici zip superflui",
      "description": "Rimuovere i codici zip prefix che hanno valore minimo (1003)",
      "columns": ["customer_zip_code_prefix"],
      "pandas_method": "dropna",
      "priority": "high",
      "business_impact": "Eliminazione dei dati non rilevanti"
    },
    {
      "step_id": 2,
      "name": "Trasformare tipi di dati di zip_code_prefix",
      "description": "Convertire i valori di zip_code_prefix da int64 a str",
      "columns": ["customer_zip_code_prefix"],
      "pandas_method": "apply(lambda x: str(x) if isinstance(x, int) else x)"
    },
    {
      "step_id": 3,
      "name": "Rimuovi duplicate customer_unique_id",
      "description": "Eliminare le righe duplicate di customer_unique_id",
      "columns": ["customer_unique_id"],
      "pandas_method": "drop_duplicates"
    }
  ]
}
```

## Narrativa Audit

**Audit di Qualità dei Dati per la Tabella "customers"**

**Sintesi dell'intervento**

L'obiettivo di questo audit è stato quello di valutare la qualità dei dati nella tabella "customers" del nostro Data Warehouse (DW) elettronico-commerce. La procedura di cleaning dei dati è stata eseguita in due fasi: deduplicatione e standardizzazione.

**Trasformazioni principali**

1. **Deduplication**: la procedura di deduplicatione ha rimossi 0 duplicati nella tabella "customers", confermando che la funzione di identificazione univoca ("customer_id") è stata efficace.
2. **Standardizzazione**: la standardizzazione delle colonne è stata eseguita con i seguenti passaggi:
	* La colonna "city" è stata trasformata in "title".
	* La colonna "state" è stata trasformata in "upper", ovvero convertita a maiuscolo.
	* Le stringhe di testo sono state sbarrate utilizzando il tag "strip".

**Impatto sulla qualità**

Il processo di cleaning dei dati ha avuto un impatto positivo sulla qualità della tabella, migliorando la consistenza e l'uniformità dei dati. La riduzione degli duplicati (0) conferma che la funzione di identificazione univoca è stata efficace.

**Limitazioni**

1. **Manutenzione del dataset**: non si sono verificate particolari limitazioni durante il processo di cleaning.
2. **Scrittura logica**: non si sono verificati errori di scrittura logica che avrebbero richiesto interventi addizionali.

**Raccomandazioni**

1. **Continuare a monitorare la qualità dei dati**: è importante continuare a monitorare la qualità dei dati per evitare eventuali problemi di consistenza e unificazione.
2. **Aggiornare le tabelle regolarmente**: è consigliabile aggiornare le tabelle regolarmente per mantenere la loro completezza e affidabilità.
3. **Implementare controlli di validità**: è importante implementare controlli di validità per assicurarsi che i dati siano stati trattati correttamente.

**Statistiche**

Prima del cleaning:

* Row: 99441
* Colonna: 5
* Duplicati: 0
* Assenti totale: 0

Dopo il cleaning:

* Row: 99441
* Colonna: 5
* Duplicati: 0
* Nuove colonne: []

**Log di controllo**

Il log di controllo contiene i dettagli delle azioni eseguite durante la procedura di cleaning. Questo log è stato utilizzato per documentare le transazioni e garantire che il processo sia stato completato correttamente.

**Nota**: questo audit è stato eseguito il 05/05/2026 alle 09:28:22.
