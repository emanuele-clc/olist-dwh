# DQ Audit - orders

## Audit Tecnico

### Panoramica

La qualità dei dati nella tabella `orders` di Olist è buona, con una percentuale bassa di valori null e un numero zero di duplicati. Tuttavia, ci sono alcune colonne che potrebbero essere oggetto di attenzione per garantire una maggiore precisione e completazza dei dati.

### Problemi rilevati

1. **Valori null nella colonna `order_approved_at`**: 0,2% dei valori sono null, il che può indicare un problema con la gestione degli ordini approvati.
2. **Valori null nella colonna `order_estimated_delivery_date`**: 0,0% dei valori sono null, ma potrebbe essere utile controllare se ci sono dati mancanti o errori nel calcolo della data di consegna stimata.
3. **Valore null nella colonna `order_delivered_customer_date`**: 3,0% dei valori sono null, il che può indicare un problema con la gestione delle date di consegna ai clienti.

### Raccomandazioni

1. **Verifica la logica di approvazione degli ordini**: controlla se ci sono regole specifiche per l'approvazione degli ordini e se i valori null nella colonna `order_approved_at` indicano un problema con questa logica.
2. **Controlla la gestione della data di consegna stimata**: assicurati che i dati di `order_estimated_delivery_date` siano corretti e aggiornati regolarmente.
3. **Verifica la gestione delle date di consegna ai clienti**: controlla se ci sono errori nella gestione delle date di consegna ai clienti e se i valori null nella colonna `order_delivered_customer_date` indicano un problema con questo processo.

In generale, è importante continuare a monitorare la qualità dei dati nella tabella `orders` e prendere azioni correttive per garantire una maggiore precisione e completazza dei dati.

## Regole di Qualita

Ecco 8 regole di qualità dati formali per la tabella orders:

**Regola 1: Riga con status ordine non null**
RULE_ID: REG_001
Colonna: order_status
Tipo: Completezza
Descrizione: La colonna "order_status" non può contenere valore nullo.
Soglia: 0

**Regola 2: Unica riga per ogni identificatore di ordine**
RULE_ID: REG_002
Colonna: order_id, customer_id
Tipo: Unicità
Descrizione: Nessuna duplicità di riga con identificatori "order_id" e "customer_id" diversi.
Soglia: 0

**Regola 3: Data di approvazione non più antica della data di acquisto**
RULE_ID: REG_003
Colonna: order_approved_at, order_purchase_timestamp
Tipo: Validita
Descrizione: La data di approvazione dell'ordine deve essere più recente della data di acquisto.
Soglia: 0

**Regola 4: Data di consegna del carrier non più antica della data di approssimazione di consegna**
RULE_ID: REG_004
Colonna: order_delivered_carrier_date, order_estimated_delivery_date
Tipo: Validita
Descrizione: La data di consegna del carrier deve essere più recente o uguale alla data di approssimazione di consegna.
Soglia: 0

**Regola 5: Data di consegna al cliente non più antica della data di consegna del carrier**
RULE_ID: REG_005
Colonna: order_delivered_customer_date, order_delivered_carrier_date
Tipo: Consistenza
Descrizione: La data di consegna al cliente deve essere contemporanea o successiva alla data di consegna del carrier.
Soglia: 0

**Regola 6: Data di approssimazione di consegna non può essere più antica della data di acquisto**
RULE_ID: REG_006
Colonna: order_estimated_delivery_date, order_purchase_timestamp
Tipo: Validita
Descrizione: La data di approssimazione di consegna deve essere più recente o uguale alla data di acquisto.
Soglia: 0

**Regola 7: Percentuale di righe con valore null per "order_approved_at"**
RULE_ID: REG_007
Colonna: order_approved_at
Tipo: Completezza
Descrizione: La percentuale delle righe con valore nullo per la colonna "order_approved_at" deve essere inferiore o uguale a 2%.
Soglia: 0.2%

**Regola 8: Percentuale di righe con valore null per "order_delivered_carrier_date"**
RULE_ID: REG_008
Colonna: order_delivered_carrier_date
Tipo: Completezza
Descrizione: La percentuale delle righe con valore nullo per la colonna "order_delivered_carrier_date" deve essere inferiore o uguale a 1.8%.
Soglia: 1.8%

## Executive Summary

**Executive Summary**

La nostra analisi dei dati degli ordini (orders) di Olist ha rivelato alcune aree da migliorare per garantire la precisione e la completanza dei dati.

I principali risultati sono:

* Una percentuale bassa di valori null nella colonna `order_approved_at`, indicativa di una gestione efficace degli ordini approvati.
* Una piccola percentuale di valori null nella colonna `order_estimated_delivery_date`, che potrebbe essere utile controllare per verificare se ci sono dati mancanti o errori nel calcolo della data di consegna stimata.
* Una percentuale più elevata di valori null nella colonna `order_delivered_customer_date`, che potrebbe indicare un problema con la gestione degli ordini consegnati ai clienti.

Questi risultati ci suggeriscono di controllare e migliorare la qualità dei dati in queste colonne per garantire una maggiore preciszione e completanza.
