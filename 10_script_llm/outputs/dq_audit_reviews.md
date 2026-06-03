# DQ Audit - reviews

## Audit Tecnico

**Analisi della qualità dei dati di Olist**

La tabella `reviews` contiene informazioni sui commenti e le recensioni degli ordini su Olist. In questo rapporto, analizzeremo la qualità dei dati presenti nella tabella.

### Panoramica

La tabella `reviews` comprende 99.224 righe e 7 colonne. La qualità dei dati è un fattore importante per l'analisi e la decisione di business.

### Problemi rilevati

Dopo aver analizzato i dati, abbiamo identificato alcuni problemi:

*   **Presenza di dati nulli**: I dati nulli presenti nella tabella sono relativamente bassi, con un 0.0% nei seguenti campi: `review_id`, `order_id`, `review_score`, `review_creation_date` e `review_answer_timestamp`. Tuttavia, i campi `review_comment_title` e `review_comment_message` presentano una presenza di dati nulli più elevata, rispettivamente del 88.3% e del 58.7%.
*   **Duplicati**: La tabella non contiene duplicati.
*   **Statistiche numeriche**: Le statistiche numeriche (min/max/mean) suggeriscono che i valori di `review_score` sono distribuiti in modo relativamente omogeneo, con una media di 4.09.

### Raccomandazioni

In base agli risultati dell'analisi, raccomando le seguenti azioni:

1.  **Rimozione dei dati nulli**: Identifica e rimuovi i dati nulli presenti nei campi `review_comment_title` e `review_comment_message`. Ciò aiuterà a migliorare la qualità dei dati e ridurre l'incertezza.
2.  **Controllo della qualità dei commenti**: Verifica che i commenti siano accurate e rilevanti per gli ordini. Ciò potrebbe essere necessario con una revisione manuale dei dati.
3.  **Aggiornamento delle statistiche numeriche**: Continua a monitorare le statistiche numeriche per garantire che il distributore di dati sia coerente ed efficiente.

In definitiva, analizzare la qualità dei dati è un passaggio fondamentale per garantire l'accuratezza e la decisionabilità dei dati in un ambiente di e-commerce come Olist.

## Regole di Qualita

Ecco 8 regole di qualità dei dati formali per la tabella "reviews":

**Rule 1: RULE_001, review_creation_date, Completezza, Descrizione: Il campo di creazione delle recensioni non può essere vuoto**

Soglia: 0.5

Regola: Tutte le righe della tabella "reviews" dovrebbero avere un valore nel campo "review_creation_date".

**Rule 2: RULE_002, review_comment_title, Completezza, Descrizione: Il campo di titolo delle recensioni commentate non può essere vuoto**

Soglia: 0.5

Regola: Tutte le righe della tabella "reviews" dove il campo "review_comment_message" ha un valore dovrebbero avere un valore nel campo "review_comment_title".

**Rule 3: RULE_003, review_answer_timestamp, Unicita, Descrizione: Ogni timestamp di risposta alle recensioni è unico**

Soglia: 0.01

Regola: Non può esistere più di una riga nella tabella "reviews" con lo stesso valore nel campo "review_answer_timestamp".

**Rule 4: RULE_004, review_score, Valitudine, Descrizione: Il punteggio delle recensioni deve essere un numero intero tra 1 e 5**

Soglia: (1, 5)

Regola: Tutti i valori nel campo "review_score" devono essere numeri interi compresi tra 1 e 5.

**Rule 5: RULE_005, review_comment_title, Consistenza, Descrizione: Il titolo delle recensioni commentate non può essere più lungo di 100 caratteri**

Soglia: 100

Regola: Tutti i valori nel campo "review_comment_title" devono essere stringhe con lunghezza massima 100 caratteri.

**Rule 6: RULE_006, review_creation_date, Tempestivita, Descrizione: Le recensioni non possono avere una data di creazione più antica di ieri**

Soglia: -1

Regola: Tutte le righe della tabella "reviews" dove il campo "review_creation_date" è oggi o in passato dovrebbero avere una data di creazione più recente di ieri.

**Rule 7: RULE_007, review_comment_message, Valitudine, Descrizione: Il testo delle recensioni commentate non può essere vuoto**

Soglia: (non vuoto)

Regola: Tutte le righe della tabella "reviews" dove il campo "review_comment_title" ha un valore dovrebbero avere un valore nel campo "review_comment_message".

**Rule 8: RULE_008, order_id, Unicita, Descrizione: Ogni ordine non può essere associato a più di una recensione**

Soglia: 0.01

Regola: Non può esistere più di una riga nella tabella "reviews" con lo stesso valore nel campo "order_id".

## Executive Summary

**Executive Summary: Analisi della qualità dei dati di Olist**

Il nostro rapporto d'analisi esamina la tabella `reviews` contenuta nel sistema Olist, che fornisce informazioni sui commenti e le recensioni degli ordini. I nostri results tecnici hanno identificato alcuni problemi di qualità dei dati nella tabella:

*   **Dati nulli**: Sebbene i dati nulli siano relativamente bassi, la presenza di dati nulli è ancora un problema che potrebbe influenzare le analisi e le decisioni di business.
*   **Consistenza dei dati**: È importante garantire una consistenza dei dati in modo da assicurarsi l'accuratezza delle informazioni.

I dati nulli sono la causa più comune per queste problematiche. Dobbiamo sviluppare un piano per ridurre il numero di dati nulli e migliorare la qualità dei dati nella tabella `reviews`. Questo pianificazione è di base, ma potrebbe essere ulteriormente specificata in una sessione con i manager.

I dati raccolti indicano che:

*   La presenza di dati nulli non è un problema serio nel sistema.
*   Dobbiamo sviluppare un piano per ridurre la quantità dei dati nulli nella tabella `reviews`.

Il piano d'azione proposto includerà:

*   Analisi approfondita dei campi con dati nulli
*   Implementazione di controlli di validazione dei dati
*   Formazione del personale sulle best practice per la gestione dei dati
