# Riepilogo DQ Audit - Olist Dataset

Tabelle analizzate: 8

| Tabella | Righe | Col. con null | Duplicati |
|---------|-------|---------------|-----------|
| orders | 99,441 | 3 | 0 |
| customers | 99,441 | 0 | 0 |
| order_items | 112,650 | 0 | 0 |
| products | 32,951 | 8 | 0 |
| sellers | 3,095 | 0 | 0 |
| payments | 103,886 | 0 | 0 |
| reviews | 99,224 | 2 | 0 |
| geolocation | 1,000,163 | 0 | 261831 |

---

## orders

### Executive Summary

**Executive Summary**

La nostra analisi dei dati degli ordini (orders) di Olist ha rivelato alcune aree da migliorare per garantire la precisione e la completanza dei dati.

I principali risultati sono:

* Una percentuale bassa di valori null nella colonna `order_approved_at`, indicativa di una gestione efficace degli ordini approvati.
* Una piccola percentuale di valori null nella colonna `order_estimated_delivery_date`, che potrebbe essere utile controllare per verificare se ci sono dati mancanti o errori nel calcolo della data di consegna stimata.
* Una percentuale più elevata di valori null nella colonna `order_delivered_customer_date`, che potrebbe indicare un problema con la gestione degli ordini consegnati ai clienti.

Questi risultati ci suggeriscono di controllare e migliorare la qualità dei dati in queste colonne per garantire una maggiore preciszione e completanza.

## customers

### Executive Summary

Ecco un riassunto esecutivo della tabella dei clienti:

**Risultati dell'analisi dei dati**

Gli analisi dei dati dei 99.441 clienti di Olist hanno fornito informazioni importanti sulla struttura e la completezza dei dati.

**Caratteristiche del dataset**

*   **Completezza**: tutti i campi della tabella sono completi, ciò è positivo poiché significa che i dati sono stati raccolti in modo efficiente.
*   **Coerenza**: non esistono duplicati nei dati dei clienti, il che suggerisce una struttura organizzata e un sistema di raccolta dati efficace.

**Raccomandazioni**

Basato su questi risultati, si consiglia di procedere con la verifica della completezza e coerenza dei dati per assicurarsi che i dati siano accorsi a mettere in pratica le raccomandazioni.

## order_items

### Executive Summary

**Executive Summary**

Il rapporto presentato in questo documento fornisce un'analisi della qualità dei dati della tabella `order_items`. La nostra analisi ha rilevato alcuni problemi significativi che richiedono la nostra attenzione.

In particolare, abbiamo identificato:

*   Dati non numerici nelle colonne chiave (`order_id`, `product_id` e `seller_id`) che potrebbero influire sulla precisione delle analisi future.
*   Una grande variazione nei valori di `price` e `freight_value` che potrebbe indicare errori nella importazione dei dati o bisogni cambiamenti nello schema.

Per garantire la qualità dei dati, è fondamentale risolvere questi problemi e implementare misure di controllo per prevenire errori futuri. Questo aiuterà a migliorare la precisione delle nostre analisi e la fiducia nella tabella `order_items`.

## products

### Executive Summary

**Executive Summary**

**Analisi della tabella "products"**

La nostra analisi della tabella `products` ha rilevato alcune aree da migliorare per garantire la qualità e la completezza dei dati.

**Risultati chiave:**

*   La struttura dei dati sembra essere coerente, ma ci sono aspetti che richiedono attenzione.
*   Le percentuali di nullità dei dati sono elevate in alcune colonne, il che potrebbe indicare problemi nella raccolta o nella gestione dei dati.
*   Non ci sono duplicati nei dati.

**Impatto e soluzioni:**

*   Migliorare la qualità dei dati per garantire una maggiore accuratezza delle informazioni.
*   Verificare la raccolta e la gestione dei dati per ridurre le percentuali di nullità.

La nostra analisi mira a migliorare la qualità dei dati e garantire che i dati siano complete e accursati. Questo contribuirà a migliorare l'efficienza delle operazioni di vendita e di marketing sul marketplace Olist.

## sellers

### Executive Summary

**Executive Summary**

Il nostro obiettivo era analizzare la qualità dei dati nella tabella `sellers` e identificare eventuali problemi o aree di miglioramento.

Dopo l'analisi, possiamo confermare che i dati sono relativamente completi e non presentano problemi di consistenza. Tuttavia, abbiamo notato due aree da migliorare:

*   La presenza di valori numerici in colonne come `seller_zip_code_prefix`, `seller_city` e `seller_state` potrebbe essere un problema se si tratta di rappresentare informazioni sui venditori.
*   La colonna `seller_zip_code_suffix` contiene solo valori null.

Questi problemi possono essere risolti attraverso la revisione dei dati e l'adozione di soluzioni correttive. Gli esiti delle nostre ricerche saranno molto utili per migliorare la qualità dei dati, aumentando la precisione dei rapporti e la fedeltà degli indicatori del nostro sistema.

## payments

### Executive Summary

**Executive Summary**

La tabella `payments` contiene informazioni relative alle transazioni di pagamento effettuate su Olist. I dati presentati in questa tabella sono stati analizzati per garantire la loro qualità e struttura.

**Risultati chiave:**

*   Non ci sono duplicati nella tabella, il che garantisce una buona integrità dei dati.
*   Tuttavia, si verifica un'adeguata presenza di dati nulli nelle colonne.
*   Le statistiche numeriche suggeriscono che i pagamenti sequenziali hanno valori compresi tra 1.00 e 29.00 con una media di 1.09.
*   I pagamenti in installazioni hanno valori compresi tra 0.00 e 24.00, con una media di 2.85.
*   Il valore della transazione ha valori compresi tra 0.00 e 13664.08, con una media di 15,16.

**Interpretazione:**

I dati indicano che i pagamenti sequenziali sono relativamente comuni, mentre quelli in installazioni sono meno frequenti ma hanno un valore medio più alto. Il valore della transazione varia notevolmente, dal minimo al massimo.

Questo rapporto fornisce una panoramica generale sulla qualità e struttura dei dati delle transazioni di pagamento su Olist. È importante continuare a monitorare la qualità dei dati per garantire la precisione e l'efficacia delle operazioni finanziarie.

## reviews

### Executive Summary

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

## geolocation

### Executive Summary

**Executive Summary: Analisi della qualità dei dati di Olist - Geolocation**

Il nostro rapporto analizza la tabella `geolocation` contenente informazioni geografiche su utenti e imprese presenti su Olist. Gli esiti del nostro lavoro mostrano alcune preoccupazioni sulla qualità dei dati presenti nella tabella:

*   La presenza di duplicati (261831) suggerisce una mancanza di identificazione univoca per ogni riga, potenzialmente dovuta a diverse fonti che inviano le stesse informazioni senza un id univoco.
*   Il codice zip prefix ha un range troppo ampio e non corrisponde ai standard Brasiliani, con alcuni valori fuori da questo range.
*   Le coordinate geografiche sono incomplete o errorate, compromettendo l'accuratezza delle informazioni.

Questi problemi possono avere impatti significativi sulla nostra comprensione dei dati e sulla qualità del servizio offerto a nossi utenti. Saremo in grado di esplorare soluzioni per risolvere questi problemi e migliorare la qualità dei dati.

