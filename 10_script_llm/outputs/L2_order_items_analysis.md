# L2 - Missing & Outlier Analysis: order_items

**Data:** 2026-05-09 11:38 | **Provider:** ollama

## Valori Mancanti

```json
{}
```

### Interpretazione LLM

Nessun valore mancante rilevato in questa tabella.

## Outlier

```json
[
  {
    "column": "price",
    "method": "IQR",
    "n_outliers": 8427,
    "pct": 7.48,
    "lower_bound": -102.6,
    "upper_bound": 277.4,
    "min": 0.85,
    "max": 6735.0
  },
  {
    "column": "freight_value",
    "method": "IQR",
    "n_outliers": 12134,
    "pct": 10.77,
    "lower_bound": 0.98,
    "upper_bound": 33.25,
    "min": 0.0,
    "max": 409.68
  }
]
```

### Narrativa LLM

Sulla base dei risultati di outlier detection, ecco le analisi dettagliate per ogni colonna con outlier:

**Colonna "price"**

* Cause plausibili:
 + Esempi estremi di prezzo: potrebbe essere dovuto a un errore di input o a una specifica offerta promozionale che non è stata correttamente registrata.
 + Prezzi irregolari per prodotti o servizi: potrebbe essere dovuto a una malfattura della catena di fornitura o a una mancanza di standardizzazione dei prezzi.
* Impatto sul DW:
 + Le vendite anomale possono influenzare la strategia di marketing e di promozione, poiché le offerte possono non rappresentare con esattezza il valore reale dei prodotti o servizi.
 + La gestione delle dipendenze potrebbe essere difficile a causa della mancanza di dati rappresentativi del mercato.
* Strategia raccomandata:
 + Verificare i dati di input e correggere eventuali errori o irregolarità.
 + Analizzare le offerte promozionali e verificare se sono state regolari e representative dei prezzi normali.
 + Considerare l'adozione di un sistema di gestione dei prezzi più flessibile per consentire una maggiore flexibilità nella strategia di marketing.

**Colonna "freight_value"**

* Cause plausibili:
 + Esempi estremi di valori di spedizione: potrebbe essere dovuto a un errore di input o a una malfattura della catena di spedizione.
 + Valori irregolari di spedizione per prodotti o servizi: potrebbe essere dovuto a una mancanza di standardizzazione dei prezzi delle spedizioni.
* Impatto sul DW:
 + I costi di spedizione anomali possono influenzare la strategia di pricing e di gestione delle dipendenze, poiché i costi non rappresentano con esattezza il valore reale della spedizione.
 + La gestione delle dipendenze potrebbe essere difficile a causa della mancanza di dati rappresentativi dei costi di spedizione.
* Strategia raccomandata:
 + Verificare i dati di input e correggere eventuali errori o irregolarità.
 + Analizzare le strategie di pricing e verificare se sono state regolari e representative del valore reale della spedizione.
 + Considerare l'adozione di un sistema di gestione dei costi di spedizione più flessibile per consentire una maggiore flexibilità nella strategia di gestione delle dipendenze.

In generale, è fondamentale verificare i dati di input e assicurarsi che siano regolari e representative del valore reale dei prodotti o servizi. Inoltre, considerare l'adozione di sistemi più flessibili per consentire una maggiore flexibilità nella strategia di gestione delle dipendenze e di marketing.
