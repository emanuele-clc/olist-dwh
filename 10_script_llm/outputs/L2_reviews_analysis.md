# L2 - Missing & Outlier Analysis: reviews

**Data:** 2026-05-09 11:45 | **Provider:** ollama

## Valori Mancanti

```json
{
  "review_comment_title": {
    "pct": 88.34,
    "type": "MAR"
  },
  "review_comment_message": {
    "pct": 58.7,
    "type": "MAR"
  }
}
```

### Interpretazione LLM

Ecco la classificazione dei valori mancanti per ogni colonna:

**review_comment_title**

* **Type:** MAR (Mancanza di Relazione Assortativa Lineare)
* **Motivazione:** Il titolo della recensione è una stringa testuale, quindi può avere un impatto significativo sulla capacità di analizzare le recensioni e comprenderne il contenuto. Una mappa di valori mancanti potrebbe non essere sufficiente per gestire questa colonna.
* **Strategia raccomandata:** flagging e approfondimento del contenuto, poiché la mancanza di un titolo potrebbe influire sulla qualità delle recensioni.

**review_comment_message**

* **Type:** MAR (Mancanza di Relazione Assortativa Lineare)
* **Motivazione:** Il testo della recensione è una stringa testuale, quindi può avere un impatto significativo sulla capacità di analizzare le recensioni e comprenderne il contenuto. Una mappa di valori mancanti potrebbe non essere sufficiente per gestire questa colonna.
* **Strategia raccomandata:** flagging e approfondimento del contenuto, poiché la mancanza di un testo potrebbe influire sulla qualità delle recensioni.

**product_id**

* **Type:** MCAR (Mancanza di Relazione Assortativa Lineare) o MAR (Mancanza di Ripetizione)
* **Motivazione:** La colonna `product_id` non è una stringa testuale, quindi potrebbe essere trattata come data o timestamp. In questo caso, la mancanza di valore potrebbe essere gestita utilizzando una strategia di imputazione.
* **Strategia raccomandata:** imputazione usando un algoritmo di impiegamento lineare (ad esempio, impiegamento mean) o utilizzando un modello di prevenzione.

**product_category**

* **Type:** MAR (Mancanza di Ripetizione)
* **Motivazione:** La colonna `product_category` potrebbe essere trattata come una categorizzazione dei prodotti. In questo caso, la mancanza di valore potrebbe essere gestita utilizzando una strategia di imputazione.
* **Strategia raccomandata:** imputazione usando un algoritmo di impiegamento lineare (ad esempio, impiegamento mean) o utilizzando un modello di prevenzione.

**seller_id**

* **Type:** MAR (Mancanza di Ripetizione)
* **Motivazione:** La colonna `seller_id` potrebbe essere trattata come una identificazione dei venditori. In questo caso, la mancanza di valore potrebbe essere gestita utilizzando una strategia di imputazione.
* **Strategia raccomandata:** imputazione usando un algoritmo di impiegamento lineare (ad esempio, impiegamento mean) o utilizzando un modello di prevenzione.

**order_id**

* **Type:** MAR (Mancanza di Ripetizione)
* **Motivazione:** La colonna `order_id` potrebbe essere trattata come un'identificazione degli ordini. In questo caso, la mancanza di valore potrebbe essere gestita utilizzando una strategia di imputazione.
* **Strategia raccomandata:** imputazione usando un algoritmo di impiegamento lineare (ad esempio, impiegamento mean) o utilizzando un modello di prevenzione.

In generale, per ogni colonna che potrebbe essere trattata come una stringa testuale, la strategia raccomandata è flagging e approfondimento del contenuto. Per le colonne che potrebbero essere tratate come data o timestamp, la strategia raccomandata è imputazione usando un algoritmo di impiegamento lineare o utilizzando un modello di prevenzione.

Inoltre, per ogni colonna con mancanza di valore, è importante considerare le seguenti strategie:

* **Flagging**: segnalare la presenza di valori mancanti e richiedere ai dati di essere corretti.
* **Imputazione**: sostituire i valori mancanti con un nuovo valore appropriato (ad esempio, impiegamento mean o utilizzo di un modello di prevenzione).
* **Esclusione**: escludere le righe con valori mancanti dal dataset.

La scelta della strategia dipenderà dalle specifiche esigenze del progetto e dai requisiti del business.

## Outlier

```json
[
  {
    "column": "review_score",
    "method": "IQR",
    "n_outliers": 14575,
    "pct": 14.69,
    "lower_bound": 2.5,
    "upper_bound": 6.5,
    "min": 1.0,
    "max": 5.0
  }
]
```

### Narrativa LLM

**Risultati di outlier detection per la tabella reviews**

Siamo stati in grado di identificare un numero significativo di outliers nella tabella `reviews`, che rappresentano circa il 14,69% delle righe totali.

**Colonna "review_score"**

Nel contesto di Olist, il punteggio della recensione è un fattore importante per determinare la credibilità e l'autenticità dei venditori. Gli outliers in questa colonna potrebbero essere causati da vari fattori, come ad esempio:

*   **Errori di input**: possibili errori nell'input del punteggio della recensione
*   **Cattive recensioni**: recensioni negative che possono essere state ingannevolmente segnalate come positive
*   **Recensioni fake**: recensioni artificiali o fake che sono state inserite nel sistema

L'impatto sulle vendite di Olist potrebbe essere significativo, poiché un punteggio della recensione eccessivamente alto può influenzare la credibilità dei venditori. Questo, a sua volta, potrebbe ridurre la fiducia dei clienti nei confronti del marketplace.

**Strategie raccomandate:**

1.  **Flagging**: identificare e segnalare gli outlier per un eventuale controllo più approfondito
2.  **Cap:** esaminare attentamente i dati dei punteggi della recensione e cercare eventuali modelli di comportamento non normale
3.  **Rimozione**: considerare la possibilità di rimuovere i dati outlier se sono stati identificati come falsi o ingannevoli
