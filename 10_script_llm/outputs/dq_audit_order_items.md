# DQ Audit - order_items

## Audit Tecnico

### Analisi della qualità dei dati di Olist - Tabella order_items

La tabella `order_items` contiene 112.650 righe e 7 colonne. In questo rapporto, ecco i risultati dell'analisi della qualità dei dati:

#### Panoramica
La tabella presenta una buona qualità generale, con poche presenze di nullità nelle colonne. Tuttavia, è necessario effettuare ulteriori analisi per capire se esistono altre problematiche.

#### Problemi rilevati
Il problema più evidente è la presenza di dati non numerici nelle colonne `order_id`, `product_id` e `seller_id`. Questo potrebbe essere dovuto a una mancanza di standardizzazione dei dati o ad un errore durante il processo di importazione.

Inoltre, le statistiche numeriche mostrano una grande variazione nei valori di `price` e `freight_value`, che potrebbero indicare problemi con la normalizzazione dei prezzi o il calcolo del valore della spesa.

#### Raccomandazioni
Per migliorare la qualità dei dati, si consiglia:

1. **Standardizzare i dati**: assicurarsi che le colonne `order_id`, `product_id` e `seller_id` contengano solo valori numerici.
2. **Verificare i prezzi**: controllare se esistono errori nel calcolo del prezzo o nella normalizzazione dei prezzi.
3. **Calcolare il valore della spesa**: verificare se l'operazione di calcolo del `freight_value` è corretta e se i dati sono stati importati correttamente.

Inoltre, potrebbe essere utile effettuare ulteriori analisi sui dati per capire se esistono altre problematiche o opportunità per migliorare la qualità dei dati.

## Regole di Qualita

Ecco 8 regole di qualità dei dati formali per la tabella `order_items`:

**REGOLA 1**
RULE_ID: QD_01
Colonna: order_id
Tipo: Completezza
Descrizione: Ogni ordine deve avere un ID univoco.
Soglia: Non null

**REGOLA 2**
RULE_ID: QD_02
Colonna: product_id
Tipo: Unicità
Descrizione: Ogni prodotto all'interno di un ordine deve avere un ID univoco.
Soglia: Non null, Valore unico (non ripetuto)

**REGOLA 3**
RULE_ID: QD_03
Colonna: shipping_limit_date
Tipo: Validita
Descrizione: La data di scadenza del carrello deve essere una data valida.
Soglia: Data valida (inserisci una data entro un certo periodo, ad esempio la fine dell'anno)

**REGOLA 4**
RULE_ID: QD_04
Colonna: freight_value
Tipo: Validita
Descrizione: Il valore del carico deve essere positivo.
Soglia: Valore positivo (inserisci un valore non negativo)

**REGOLA 5**
RULE_ID: QD_05
Colonna: order_item_id
Tipo: Unicità
Descrizione: Ogni ordine item deve avere un ID univoco all'interno di un ordine.
Soglia: Non null, Valore unico (non ripetuto)

**REGOLA 6**
RULE_ID: QD_06
Colonna: seller_id
Tipo: Unicità
Descrizione: Ogni venditore all'interno di un ordine deve avere un ID univoco.
Soglia: Non null, Valore unico (non ripetuto)

**REGOLA 7**
RULE_ID: QD_07
Colonna: price
Tipo: Validita
Descrizione: Il prezzo dell'ordine item deve essere positivo.
Soglia: Valore positivo (inserisci un valore non negativo)

**REGOLA 8**
RULE_ID: QD_08
Colonna: freight_value > 0
Tipo: Consistenza
Descrizione: Il carico non può essere zero o negativo, in quanto sarebbe impossibile per il venditore.
Soglia: Non null, Valore positivo

## Executive Summary

**Executive Summary**

Il rapporto presentato in questo documento fornisce un'analisi della qualità dei dati della tabella `order_items`. La nostra analisi ha rilevato alcuni problemi significativi che richiedono la nostra attenzione.

In particolare, abbiamo identificato:

*   Dati non numerici nelle colonne chiave (`order_id`, `product_id` e `seller_id`) che potrebbero influire sulla precisione delle analisi future.
*   Una grande variazione nei valori di `price` e `freight_value` che potrebbe indicare errori nella importazione dei dati o bisogni cambiamenti nello schema.

Per garantire la qualità dei dati, è fondamentale risolvere questi problemi e implementare misure di controllo per prevenire errori futuri. Questo aiuterà a migliorare la precisione delle nostre analisi e la fiducia nella tabella `order_items`.
