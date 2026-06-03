# L2 - Missing & Outlier Analysis: orders

**Data:** 2026-05-09 11:37 | **Provider:** ollama

## Valori Mancanti

```json
{
  "order_approved_at": {
    "pct": 0.16,
    "type": "MCAR"
  },
  "order_delivered_carrier_date": {
    "pct": 1.79,
    "type": "MAR"
  },
  "order_delivered_customer_date": {
    "pct": 2.98,
    "type": "MAR"
  }
}
```

### Interpretazione LLM

Ecco le classificazioni per ciascuna colonna:

**1. order_approved_at**

* Pct: 0.16
* Tipo: MCAR (Missing Completely at Random)
* Motivazione: I dati di approvazione degli ordini sono completamente casuali e non sono influenzati da fattori esterni, quindi è probabile che si tratti di una variabile casuale.
* Impatto sul DW: Nessun impatto significativo, poiché la variabile è indipendente dal resto del dataset.
* Strategia raccomandata: **Esclusione** - non è necessario gestire i dati mancanti per evitare effetti di selezione.

**2. order_delivered_carrier_date**

* Pct: 1.79
* Tipo: MAR (Missing At Random)
* Motivazione: I dati della data di consegna del carrier sono casuali e non dipendono da fattori esterni, ma potrebbero essere influenzati da fattori interni al dataset.
* Impatto sul DW: Alcun impatto, poiché la variabile potrebbe essere correlata con altre variabili che influenzano la consegna dei prodotti.
* Strategia raccomandata: **Imputazione** - è consigliabile immettere una valuta probabile per la data di consegna del carrier, ad esempio il giorno successivo all'ordine.

**3. order_delivered_customer_date**

* Pct: 2.98
* Tipo: MAR (Missing At Random)
* Motivazione: I dati della data di consegna del cliente sono casuali e non dipendono da fattori esterni, ma potrebbero essere influenzati da fattori interni al dataset.
* Impatto sul DW: Alcun impatto, poiché la variabile potrebbe essere correlata con altre variabili che influenzano la consegna dei prodotti.
* Strategia raccomandata: **Imputazione** - è consigliabile immettere una valuta probabile per la data di consegna del cliente, ad esempio il giorno successivo all'ordine.

In generale, le strategie di gestione dei dati mancanti possono essere:

* Esclusione: utilizzare solo i dati completi e escludere quelli mancanti.
* Imputazione: immettere valuti probabili per i dati mancanti, ad esempio basati sulla media o sulla distribuzione della variabile.
* Flagging: creare un flag per indicare se la variabile è presente o mancante, in modo che possa essere gestita separatamente.

In questo caso, considerando l'impatto sul DW e la motivazione domain-aware, consiglio di utilizzare imputazione per le colonne `order_delivered_carrier_date` e `order_delivered_customer_date`, mentre escludere la colonna `order_approved_at`.

## Outlier

```json
[]
```

### Narrativa LLM

Nessun outlier significativo rilevato in questa tabella.
