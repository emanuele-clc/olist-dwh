# DQ Audit - customers

## Audit Tecnico

**Panoramica**

I dati dei clienti di Olist presentano alcune caratteristiche interessanti. La tabella contiene informazioni su 99.441 clienti, con una struttura composta da cinque colonne. I dati sono rappresentati in diversi formati, tra cui numerici e stringa.

**Problemi rilevati**

Ecco alcuni problemi rilevati durante l'analisi dei dati:

*   **Presenza di nullità**: non ci sono nullità nelle colonne date. Ciò è positivo poiché indica che i dati erano più completi o garantita un'applicazione e/o struttura data.
*   **Duplicati**: non ci sono duplicati nei dati dei clienti. Questo suggerisce che la tabella è coerente e i dati sono ben organizzati.

**Raccomandazioni**

In base agli risultati dell'analisi, le seguenti raccomandazioni possono essere fatte:

*   **Verificare la correttezza degli zip code**: il range dei zip code preso in considerazione è molto ampio (da 1003.00 a 99990.00). Tuttavia, alcuni di questi zip code potrebbero non essere validi o essere stati esclusi per motivi legali o tecnici.
*   **Utilizzare un sistema di codice zip codice standardizzato**: per garantire la correttezza e il completamento dei dati, utilizzare un sistema di codice zip codice standardizzato può aiutare a ridurre gli errori.

## Regole di Qualita

Ecco 7 regole di qualità dati formali per la tabella "customers":

**Regola 1**
RULE_ID-Customer_ID-Completezza-Soglia: 90
Descrizione: Tutti i record della colonna "customer_id" devono avere un valore non null.
Soglia: 90%

**Regola 2**
RULE_ID-CustomerUniqueId-Unicità-Soglia: 0.5
Descrizione: Nessun record della colonna "customer_unique_id" deve avere lo stesso valore di più di una volta.
Soglia: 0,5 (il 50% dei record devono essere unici)

**Regola 3**
RULE_ID-CustomerZipCodePrefix-Validita-Soglia: 'US-00'
Descrizione: Tutti i record della colonna "customer_zip_code_prefix" devono avere un valore che inizia con 'US-' (codice ZIP di Stati Uniti).
Soglia: La stringa deve iniziare con le tre lettere 'US-' seguite da una cifra tra 00 e 99.

**Regola 4**
RULE_ID-CustomerCity-Validita-Soglia: '^[A-Z]{1,2}[0-9R]{0,3}$'
Descrizione: Tutti i record della colonna "customer_city" devono avere un valore che inizia con una lettera (A-Z) o la lettera 'R' e seguito da zero o tre cifre.
Soglia: La stringa deve soddisfare il pattern espresso dalla regola.

**Regola 5**
RULE_ID-CustomerState-Validita-Soglia: '^[A-Z]{2}$'
Descrizione: Tutti i record della colonna "customer_state" devono avere un valore che è una lettera in maiuscolo (A-Z) seguito da una lettera in maiuscolo.
Soglia: La stringa deve soddisfare il pattern espresso dalla regola.

**Regola 6**
RULE_ID-CustomerZipCodePrefix-Consistenza-Soglia: 90
Descrizione: Nessun record della colonna "customer_zip_code_prefix" può avere due o più valori diversi.
Soglia: 90% (il 90% dei record deve avere un valore unico)

**Regola 7**
RULE_ID-CustomerUniqueId-Consistenza-Soglia: 0.5
Descrizione: Nessun record della colonna "customer_unique_id" può avere lo stesso valore di più di una volta.
Soglia: 0,5 (il 50% dei record devono essere unici)

Nota che queste regole sono solo esempi e potrebbero dover essere adattate alle esigenze specifiche del tuo progetto.

## Executive Summary

Ecco un riassunto esecutivo della tabella dei clienti:

**Risultati dell'analisi dei dati**

Gli analisi dei dati dei 99.441 clienti di Olist hanno fornito informazioni importanti sulla struttura e la completezza dei dati.

**Caratteristiche del dataset**

*   **Completezza**: tutti i campi della tabella sono completi, ciò è positivo poiché significa che i dati sono stati raccolti in modo efficiente.
*   **Coerenza**: non esistono duplicati nei dati dei clienti, il che suggerisce una struttura organizzata e un sistema di raccolta dati efficace.

**Raccomandazioni**

Basato su questi risultati, si consiglia di procedere con la verifica della completezza e coerenza dei dati per assicurarsi che i dati siano accorsi a mettere in pratica le raccomandazioni.
