# L3 - Cleaning: sellers

**Data:** 2026-05-09 11:56 | **Provider:** ollama

## Piano di Cleaning

```json
{
  "table": "sellers",
  "steps": [
    {
      "step_id": 1,
      "name": "Cleansing di seller_id",
      "description": "Rimuovi i dati non numeriche e trasformi i valori in numerici.",
      "columns": ["seller_id"],
      "pandas_method": "clean_string",
      "priority": "high",
      "business_impact": "Rimozione dei dati non utilizzabili"
    },
    {
      "step_id": 2,
      "name": "Cleansing di seller_zip_code_prefix",
      "description": "Trasforma i valori della colonna zip_code_prefix in stringhe con 5 caratteri.",
      "columns": ["seller_zip_code_prefix"],
      "pandas_method": "pad_to_length",
      "priority": "medium",
      "business_impact": "Rimuovi le eventuali informazioni non utilizzabili"
    },
    {
      "step_id": 3,
      "name": "Cleansing di seller_city",
      "description": "Rimuovi i dati nulli e trasforma i valori in stringhe con più di 4 caratteri.",
      "columns": ["seller_city"],
      "pandas_method": "remove_null_andtruncate",
      "priority": "medium",
      "business_impact": "Rimozione dei dati non utilizzabili"
    },
    {
      "step_id": 4,
      "name": "Cleansing di seller_state",
      "description": "Rimuovi i dati nulli e trasforma i valori in stringhe con più di 2 caratteri.",
      "columns": ["seller_state"],
      "pandas_method": "remove_null_andtruncate",
      "priority": "low",
      "business_impact": "Rimozione dei dati non utilizzabili"
    }
  ]
}
```

## Narrativa Audit

**Audit della Tabella Olist "sellers"**

**Sintesi dell'intervento**
L'audit della tabella Olist "sellers" è stato eseguito per migliorare la qualità e la precisione dei dati della tabella. Lo scopo dell'audit era quello di rilevare e eliminare eventuali duplicati, standardizzare i campi dei dati e assicurarsi che la tabella fosse completa e coerente.

**Trasformazioni principali**

*   Rimozione delle duplicate: è stata eseguita un'analisi di identificazione dei duplicati nella tabella "sellers" e sono stati eliminati 0 duplicati.
*   Standardizzazione dei campi dei dati: è stata effettuata la standardizzazione dei campi "city", "state" e altri. La trasformazione includeva l'eliminazione di eventuali spazi vuoti e la conversione degli attributi in formato corretto.

**Impatto sulla qualità**
L'intervento ha avuto un impatto positivo sulla qualità della tabella "sellers". Dopo l'intervento, la tabella è risultata completa e coerente senza duplicati. La standardizzazione dei campi dei dati ha garantito che i dati siano presentati in una forma uniforme e facilmente accessibile.

**Limitazioni**

*   Possibilità di errori manuali: sebbene l'intervento abbia avuto un impatto positivo, è importante prestare attenzione a eventuali errori manuali durante il processo.
*   Manutenzione costante: la qualità della tabella può subire cambiamenti nel tempo, quindi è importante effettuare regolarmente controlli e interventi per mantenere la sua completezza e correttezza.

**Raccomandazioni**

1.  Effettuare regolarmente audit e controllo della tabella "sellers" per garantire la sua qualità e completezza.
2.  Implementare un sistema di gestione dei dati che consenta di monitorare automaticamente le transazioni e identificare eventuali duplicati o errori di tipo diverso.
3.  Considerare l'aggiunta di funzionalità di standardizzazione dei campi dei dati per garantire una uniformità nella presentazione dei dati all'interno della tabella.

In sintesi, l'intervento ha avuto un impatto positivo sulla qualità della tabella "sellers", ma è importante mantenere una routine di controllo e audit regolare per garantire la sua completezza e correttezza.
