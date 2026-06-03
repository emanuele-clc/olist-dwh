# DQ Audit - payments

## Audit Tecnico

**Analisi della qualità dei dati delle transazioni di pagamento (Olist - Payments)**

### Panoramica

La tabella `payments` contiene informazioni relative alle transazioni di pagamento effettuate su Olist. La tabella ha 103.886 righe e 5 colonne.

### Problemi rilevati

Non sono stati trovati duplicati nella tabella, il che indica una buona integrità dei dati. Tuttavia, è presente un certo livello di nullità nei dati, con un totale di 0 null (0.0%) in ogni colonna.

Le statistiche numeriche indicate suggeriscono che:

*   Il pagamento sequenziale ha valori compresi tra 1.00 e 29.00, con una media di 1.09.
*   I pagamenti in installazioni hanno valori compresi tra 0.00 e 24.00, con una media di 2.85.
*   Il valore della transazione ha valori compresi tra 0.00 e 13664.08, con una media di 154.10.

Questi risultati suggeriscono che i dati sono relativamente omogenei e coerenti, ma potrebbero essere più completi se si desidera ottenere informazioni più dettagliate sulle transazioni.

### Raccomandazioni

1.  **Verifica la completezza dei dati**: considerare l'importazione di ulteriori dati per completare le informazioni relative alle transazioni.
2.  **Controlla la consistenza dei dati**: controllare se ci sono differenze o irregolarità nei dati che potrebbero influire sulla qualità della tabella.
3.  **Optimizzazione dello schema di tabella**: considerare l'aggiunta di nuove colonne per contenere informazioni aggiuntive relative alle transazioni, come ad esempio la data dell'applicazione o il tipo di pagamento utilizzato.

In generale, i dati presentati sembrano essere coerenti e omogenei, ma ci sono spazio per migliorare la completezza e la consistenza dei dati.

## Regole di Qualita

Ecco 7 regole di qualità dati formali per la tabella "payments":

**RULE_01, order_id, Completezza, Descrizione: Tutte le colonne devono contenere l'identificatore dell'ordine**
Soglia: Il valore deve essere presente in tutti i record della tabella

**RULE_02, payment_sequential, Unicità, Descrizione: L' sequenziale del pagamento deve essere unica per ogni ordine**
Soglia: Devono esistere almeno 2 record con lo stesso valorlo di payment_sequential ed order_id diverso da quello dell'ordine corrispondente

**RULE_03, payment_type, Validita, Descrizione: Il tipo di pagamento deve essere uno dei seguenti valori**
Soglia: Il valore deve appartenersi a una delle seguenti liste: cartacash, PayPal, bank transfer, credit card, altri (specificare il valore)

**RULE_04, payment_installments, Completezza, Descrizione: Tutte le colonne devono contenere i numeri degli installamenti**
Soglia: Il valore deve essere presente in tutti i record della tabella

**RULE_05, payment_value, Unicità, Descrizione: La somma dei pagamenti deve essere unica per ogni ordine**
Soglia: Devono esistere almeno 2 record con lo stesso valorlo di payment_value ed order_id diverso da quello dell'ordine corrispondente

**RULE_06, payment_value, Consistenza, Descrizione: La somma dei pagamenti deve essere non negativa**
Soglia: Il valore deve essere ≥ 0

**RULE_07, payment_sequential, Tempestivita, Descrizione: Le date di pagamento devono essere ordinate cronologicamente**
Soglia: I record con lo stesso valorlo di payment_sequential dovrebbero avere date di pagamento successive a quella del record precedente

## Executive Summary

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
