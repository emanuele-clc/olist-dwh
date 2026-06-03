# L2 - Missing & Outlier Analysis: products

**Data:** 2026-05-09 11:42 | **Provider:** ollama

## Valori Mancanti

```json
{
  "product_category_name": {
    "pct": 1.85,
    "type": "MAR"
  },
  "product_name_lenght": {
    "pct": 1.85,
    "type": "MAR"
  },
  "product_description_lenght": {
    "pct": 1.85,
    "type": "MAR"
  },
  "product_photos_qty": {
    "pct": 1.85,
    "type": "MAR"
  },
  "product_weight_g": {
    "pct": 0.01,
    "type": "MCAR"
  },
  "product_length_cm": {
    "pct": 0.01,
    "type": "MCAR"
  },
  "product_height_cm": {
    "pct": 0.01,
    "type": "MCAR"
  },
  "product_width_cm": {
    "pct": 0.01,
    "type": "MCAR"
  }
}
```

### Interpretazione LLM

Ecco le classificazioni e raccomandazioni per ogni colonna:

**1. product_category_name**

* Pct di valori mancanti: 1.85%
* Tipo di mancanza: MAR (Mostly Missing At Random)
* Motivazione: il nome della categoria del prodotto può essere considerato come una variabile non significativa rispetto all'ordine di acquisto o ad altri fattori relativi al cliente.
* Impatto sul DW: riduzione della precisione delle analisi, poiché la mancanza di informazioni sulla categoria potrebbe influenzare le previsioni dei valori futuri.
* Strategia raccomandata: flag, con l'obiettivo di identificare ordini correlati con ordini senza valore mancante.

**2. product_name_lenght**

* Pct di valori mancanti: 1.85%
* Tipo di mancanza: MAR (Mostly Missing At Random)
* Motivazione: la lunghezza del nome del prodotto può essere considerata come una variabile non significativa rispetto al valore della transazione o al cliente.
* Impatto sul DW: riduzione della precisione delle analisi, poiché la mancanza di informazioni sulla lunghezza del nome potrebbe influenzare le previsioni dei valori futuri.
* Strategia raccomandata: flag, con l'obiettivo di identificare ordini correlati con ordini senza valore mancante.

**3. product_description_lenght**

* Pct di valori mancanti: 1.85%
* Tipo di mancanza: MAR (Mostly Missing At Random)
* Motivazione: la lunghezza della descrizione del prodotto può essere considerata come una variabile non significativa rispetto al valore della transazione o al cliente.
* Impatto sul DW: riduzione della precisione delle analisi, poiché la mancanza di informazioni sulla lunghezza della descrizione potrebbe influenzare le previsioni dei valori futuri.
* Strategia raccomandata: flag, con l'obiettivo di identificare ordini correlati con ordini senza valore mancante.

**4. product_photos_qty**

* Pct di valori mancanti: 1.85%
* Tipo di mancanza: MAR (Mostly Missing At Random)
* Motivazione: la quantità di foto del prodotto può essere considerata come una variabile non significativa rispetto al valore della transazione o al cliente.
* Impatto sul DW: riduzione della precisione delle analisi, poiché la mancanza di informazioni sulla quantità di foto potrebbe influenzare le previsioni dei valori futuri.
* Strategia raccomandata: flag, con l'obiettivo di identificare ordini correlati con ordini senza valore mancante.

**5. product_weight_g**

* Pct di valori mancanti: 0.01%
* Tipo di mancanza: MCAR (Missing Completely At Random)
* Motivazione: la massa in grammi del prodotto è una variabile significativa che può influenzare il valore della transazione e il comportamento del cliente.
* Impatto sul DW: riduzione della precisione delle analisi, poiché la mancanza di informazioni sulla massa potrebbe influenzare le previsioni dei valori futuri.
* Strategia raccomandata: imputazione, utilizzando la media ponderata per immettere un valore plausibile.

**6. product_length_cm**

* Pct di valori mancanti: 0.01%
* Tipo di mancanza: MCAR (Missing Completely At Random)
* Motivazione: la lunghezza in centimetri del prodotto è una variabile significativa che può influenzare il valore della transazione e il comportamento del cliente.
* Impatto sul DW: riduzione della precisione delle analisi, poiché la mancanza di informazioni sulla lunghezza potrebbe influenzare le previsioni dei valori futuri.
* Strategia raccomandata: imputazione, utilizzando la media ponderata per immettere un valore plausibile.

**7. product_height_cm**

* Pct di valori mancanti: 0.01%
* Tipo di mancanza: MCAR (Missing Completely At Random)
* Motivazione: l'altezza in centimetri del prodotto è una variabile significativa che può influenzare il valore della transazione e il comportamento del cliente.
* Impatto sul DW: riduzione della precisione delle analisi, poiché la mancanza di informazioni sull'altezza potrebbe influenzare le previsioni dei valori futuri.
* Strategia raccomandata: imputazione, utilizzando la media ponderata per immettere un valore plausibile.

**8. product_width_cm**

* Pct di valori mancanti: 0.01%
* Tipo di mancanza: MCAR (Missing Completely At Random)
* Motivazione: l'altezza in centimetri del prodotto è una variabile significativa che può influenzare il valore della transazione e il comportamento del cliente.
* Impatto sul DW: riduzione della precisione delle analisi, poiché la mancanza di informazioni sull'altezza potrebbe influenzare le previsioni dei valori futuri.
* Strategia raccomandata: imputazione, utilizzando la media ponderata per immettere un valore plausibile.

In generale, è consigliabile seguire le seguenti strategie:

* Flag per identificare ordini correlati con ordini senza valore mancante.
* Imputazione per i campi che sono significativi e possono influenzare il valore della transazione o il comportamento del cliente (ad esempio, massa in grammi, lunghezza, altezza e larghezza).
* Esclusione per i campi che non sono significativi e non possono influenzare il valore della transazione o il comportamento del cliente.

## Outlier

```json
[
  {
    "column": "product_name_lenght",
    "method": "IQR",
    "n_outliers": 290,
    "pct": 0.88,
    "lower_bound": 19.5,
    "upper_bound": 79.5,
    "min": 5.0,
    "max": 76.0
  },
  {
    "column": "product_description_lenght",
    "method": "IQR",
    "n_outliers": 2078,
    "pct": 6.31,
    "lower_bound": -610.5,
    "upper_bound": 1921.5,
    "min": 4.0,
    "max": 3992.0
  },
  {
    "column": "product_photos_qty",
    "method": "IQR",
    "n_outliers": 849,
    "pct": 2.58,
    "lower_bound": -2.0,
    "upper_bound": 6.0,
    "min": 1.0,
    "max": 20.0
  },
  {
    "column": "product_weight_g",
    "method": "IQR",
    "n_outliers": 4551,
    "pct": 13.81,
    "lower_bound": -2100.0,
    "upper_bound": 4300.0,
    "min": 0.0,
    "max": 40425.0
  },
  {
    "column": "product_length_cm",
    "method": "IQR",
    "n_outliers": 1380,
    "pct": 4.19,
    "lower_bound": -12.0,
    "upper_bound": 68.0,
    "min": 7.0,
    "max": 105.0
  },
  {
    "column": "product_height_cm",
    "method": "IQR",
    "n_outliers": 1892,
    "pct": 5.74,
    "lower_bound": -11.5,
    "upper_bound": 40.5,
    "min": 2.0,
    "max": 105.0
  },
  {
    "column": "product_width_cm",
    "method": "IQR",
    "n_outliers": 912,
    "pct": 2.77,
    "lower_bound": -7.5,
    "upper_bound": 52.5,
    "min": 6.0,
    "max": 118.0
  }
]
```

### Narrativa LLM

Ecco una possibile analisi dei risultati di outlier detection per ciascuna colonne:

**1. product_name_lenght**

* Cause plausibili:
	+ Errori di input durante la creazione dei prodotti
	+ Dati provenienti da fonti esterne non controllate
	+ Utilizzo di caratteri non standard o speciali
* Impatto sul DW: potrebbe influire sulla visibilità e sulla trovare dei prodotti, poiché i nomi dei prodotti sono importanti per la navigazione e la ricerca.
* Strategia raccomandata:
	+ Verificare che i nomi dei prodotti contengano solo caratteri standard e siano stati inseriti correttamente
	+ Utilizzare un filtro automatico per rimuovere i valori fuori range
	+ Considerare l'utilizzo di un'architettura di contenuti con più categorizzazioni per ridurre la soglia di outlier

**2. product_description_lenght**

* Cause plausibili:
	+ Errori di input durante la creazione dei prodotti
	+ Dati provenienti da fonti esterne non controllate
	+ Utilizzo di caratteri non standard o speciali
* Impatto sul DW: potrebbe influire sulla visibilità e sulla trovare dei prodotti, poiché i descrizioni dei prodotti sono importanti per la navigazione e la ricerca.
* Strategia raccomandata:
	+ Verificare che le descrizioni dei prodotti contengano solo caratteri standard e siano state inserite correttamente
	+ Utilizzare un filtro automatico per rimuovere i valori fuori range
	+ Considerare l'utilizzo di un'architettura di contenuti con più categorizzazioni per ridurre la soglia di outlier

**3. product_photos_qty**

* Cause plausibili:
	+ Errore durante il caricamento delle foto dei prodotti
	+ Dati provenienti da fonti esterne non controllate
	+ Utilizzo di immagini non presentabili o di dimensioni eccessive
* Impatto sul DW: potrebbe influire sulla visibilità e sulla trovare dei prodotti, poiché le foto dei prodotti sono importanti per la visualizzazione.
* Strategia raccomandata:
	+ Verificare che le immagini dei prodotti siano presentabili e abbiano dimensioni corrette
	+ Utilizzare un filtro automatico per rimuovere i valori fuori range
	+ Considerare l'utilizzo di un sistema di caricamento automatico delle foto dei prodotti

**4. product_weight_g**

* Cause plausibili:
	+ Errore durante il caricamento dei dati dei prodotti
	+ Dati provenienti da fonti esterne non controllate
	+ Utilizzo di valori non standard o fuorvianti per la misura del peso
* Impatto sul DW: potrebbe influire sulla qualità della ricerca e sulla visibilità dei prodotti, poiché i prezzi e le caratteristiche dei prodotti sono importanti per gli acquirenti.
* Strategia raccomandata:
	+ Verificare che i valori del peso dei prodotti siano corretti e coerenti
	+ Utilizzare un filtro automatico per rimuovere i valori fuori range
	+ Considerare l'utilizzo di un sistema di calcolo dei prezzi in base al peso

**5. product_length_cm**

* Cause plausibili:
	+ Errore durante il caricamento dei dati dei prodotti
	+ Dati provenienti da fonti esterne non controllate
	+ Utilizzo di valori non standard o fuorvianti per la misura della lunghezza
* Impatto sul DW: potrebbe influire sulla visibilità e sulla trovare dei prodotti, poiché le dimensioni dei prodotti sono importanti per la navigazione.
* Strategia raccomandata:
	+ Verificare che i valori della lunghezza dei prodotti siano corretti e coerenti
	+ Utilizzare un filtro automatico per rimuovere i valori fuori range
	+ Considerare l'utilizzo di un sistema di calcolo delle dimensioni dei prodotti

**6. product_height_cm**

* Cause plausibili:
	+ Errore durante il caricamento dei dati dei prodotti
	+ Dati provenienti da fonti esterne non controllate
	+ Utilizzo di valori non standard o fuorvianti per la misura dell'altezza
* Impatto sul DW: potrebbe influire sulla visibilità e sulla trovare dei prodotti, poiché le dimensioni dei prodotti sono importanti per la navigazione.
* Strategia raccomandata:
	+ Verificare che i valori dell'altezza dei prodotti siano corretti e coerenti
	+ Utilizzare un filtro automatico per rimuovere i valori fuori range
	+ Considerare l'utilizzo di un sistema di calcolo delle dimensioni dei prodotti

**7. product_width_cm**

* Cause plausibili:
	+ Errore durante il caricamento dei dati dei prodotti
	+ Dati provenienti da fonti esterne non controllate
	+ Utilizzo di valori non standard o fuorvianti per la misura della larghezza
* Impatto sul DW: potrebbe influire sulla visibilità e sulla trovare dei prodotti, poiché le dimensioni dei prodotti sono importanti per la navigazione.
* Strategia raccomandata:
	+ Verificare che i valori della larghezza dei prodotti siano corretti e coerenti
	+ Utilizzare un filtro automatico per rimuovere i valori fuori range
	+ Considerare l'utilizzo di un sistema di calcolo delle dimensioni dei prodotti
