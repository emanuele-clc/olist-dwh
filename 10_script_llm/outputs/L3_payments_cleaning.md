# L3 - Cleaning: payments

**Data:** 2026-05-09 11:58 | **Provider:** ollama

## Piano di Cleaning

```
{
  "table": "payments",
  "steps": [
    {
      "step_id": 1,
      "name": "Step 1: Rimozione valori nulli",
      "description": "Rimuovere le righe con valori nulli in ogni colonna",
      "columns": [],
      "pandas_method": "",
      "priority": "high",
      "business_impact": "Elimina dati aberranti e migliora la qualità dei dati"
    },
    {
      "step_id": 2,
      "name": "Step 2: Valutazione tipi di pagamenti",
      "description": "Verificare i tipi di pagamento e aggiornarli secondo le norme del business",
      "columns": [],
      "pandas_method": "",
      "priority": "high",
      "business_impact": "Garantire l'omogeneità dei dati e semplificare le analisi"
    },
    {
      "step_id": 3,
      "name": "Step 3: Normalizzazione valori di pagamento",
      "description": "Normalizzare i valori di pagamento per ottenere un range standardizzato",
      "columns": [],
      "pandas_method": "",
      "priority": "medium",
      "business_impact": "Migliorare la chiarezza dei dati e semplificare le operazioni"
    },
    {
      "step_id": 4,
      "name": "Step 4: Eliminazione duplicati",
      "description": "Eliminare le duplicate righe per prevenire errori di calcolo",
      "columns": [],
      "pandas_method": "",
      "priority": "low",
      "business_impact": "Prevenire errori di calcolo e migliorare la stabilità del sistema"
    }
  ]
}
```

## Narrativa Audit

**Audit di Data Quality per la Tabella "payments"**

**Introduzione**
L'audit di data quality per la tabella "payments" ha lo scopo di valutare l'impatto della cleaning dei dati sull'accuratezza e la qualità della tabella. Il progetto è stato eseguito sul sistema DW e-commerce, con l'obiettivo di migliorare la qualità dei dati e di ridurre gli errori.

**Sintesi dell'intervento**
L'intervento è composto da tre fasi principali:

1. **Deduplication**: sono stati rimossi 0 duplicati dalla tabella, confermando che non ci sono duplicati nel dataset originale.
2. **Standardizzazione**: le colonne "payment_type" e "payment_sequential" sono state standardizzate in formato "strip + lower", per facilitare la ricerca e l'analisi dei dati.
3. **Outlier IQR flag**: sono stati aggiunti 6 nuovi colonni alla tabella, tra cui "_payment_value_outlier", che indica se il valore della transazione è fuori dalla range di valori considerati normali.

**Trasformazioni principali**

*   Rimozione duplicati
*   Standardizzazione delle colonne "payment_type" e "payment_sequential"
*   Aggiunta dei nuovi colonni per l'outlier detection

**Impatto qualità**
L'intervento ha avuto un impatto positivo sulla qualità dei dati:

*   La tabella "payments" è risultata con 103.886 righe, senza duplicati e con solo la rimozione di eventuali valori outliers.
*   Le colonne "payment_type" e "payment_sequential" sono state standardizzate, rendendo più facile l'analisi dei dati.

**Limitazioni**
Tuttavia, ci sono alcune limitazioni da considerare:

*   La procedura di outlier detection può essere soggetta a errori, specialmente se non viene utilizzata una procedura adeguata.
*   Il campione audit log è stato molto breve e quindi potrebbe non riflettere completamente l'impatto dell'intervento sull'intera tabella.

**Raccomandazioni**

*   Utilizzare procedure di outlier detection più robuste per garantire la precisione dei risultati.
*   Esecutare campionamenti audit log più lunghi e costanti per avere un'idea più completa del impatto dell'intervento sull'intera tabella.
*   Verificare regolarmente la qualità dei dati e i risultati degli outlier detection per garantire l'accettabilità della procedura.
