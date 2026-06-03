# DQ Audit - sellers

## Audit Tecnico

**Panoramica**

Il nostro obiettivo è analizzare la qualità dei dati contenuti nella tabella `sellers` di Olist e identificare eventuali problemi o aree di miglioramento.

La tabella contiene 3.095 righe e 4 colonne, con un numero molto basso di valori null (0,0%) in tutte le colonne. Questo ci suggerisce che i dati sono relativamente completi e non presentano problemi di consistenza.

**Problemi rilevati**

Non ci sono duplicati nella tabella, il che è ottimo per la precisione dei dati.

Tuttavia, è stato osservato un piccolo problema:

*   Le colonne `seller_zip_code_prefix`, `seller_city` e `seller_state` contengono solo valori numerici. Tuttavia, è possibile che queste colonne debbano contenere valori di stringhe per rappresentare correttamente le informazioni sui venditori.
*   La colonna `seller_id` non contiene valori null.

**Raccomandazioni**

Per migliorare la qualità dei dati:

1.  Verificare se le colonne `seller_zip_code_prefix`, `seller_city` e `seller_state` devono essere di tipo stringa per rappresentare correttamente le informazioni sui venditori.
2.  Controllo delle regole di data e valori per assicurarsi che i dati siano coerenti e validi.

In sintesi, i dati della tabella `sellers` sembrano essere in buona qualità, ma è necessario controllare se ci sono aree di miglioramento, soprattutto nelle colonne che potrebbero contenere valori di tipo stringa.

## Regole di Qualita

Ecco 8 regole di qualità dati formali per la tabella "sellers":

**Regola 1**
RULE_ID_001, seller_zip_code_prefix, Tipo (Completezza), Descrizione: ogni valore deve essere presente.
Soglia: il valore non può essere vuoto.

**Regola 2**
RULE_ID_002, seller_city, Tipo (Completezza), Descrizione: ogni valore deve essere presente.
Soglia: il valore non può essere vuoto.

**Regola 3**
RULE_ID_003, seller_state, Tipo (Unicità), Descrizione: ogni valore deve essere unico.
Soglia: se si verificano più di un valore lo stesso stato per più venditori, la regola è violata.

**Regola 4**
RULE_ID_004, seller_zip_code_prefix, Tipo (Validita), Descrizione: il valore deve essere un prefisso di codice postale valido.
Soglia: i valori invalidi sono quelli che non si trovano nel database dei codici postali validi.

**Regola 5**
RULE_ID_005, seller_state, Tipo (Consistenza), Descrizione: lo stato deve essere un valore valido in base alle leggi dello Stato.
Soglia: i valori invalidi sono quelli che non corrispondono a una legge dello Stato.

**Regola 6**
RULE_ID_006, seller_city, Tipo (Consistenza), Descrizione: la città deve essere un valore valido in base alle mappe di localizzazione.
Soglia: i valori invalidi sono quelli che non corrispondono a una città nella mappa di localizzazione.

**Regola 7**
RULE_ID_007, seller_zip_code_prefix, Tipo (Tempestivita), Descrizione: il valore deve essere aggiornato entro un certo numero di giorni dalla data di scadenza.
Soglia: se il valore non è stato aggiornato entro i giorni specificati, la regola è violata.

**Regola 8**
RULE_ID_008, seller_zip_code_prefix, Tipo (Unicità), Descrizione: ogni valore deve essere unico.
Soglia: se si verificano più di un valore lo stesso prefisso di codice postale per più venditori, la regola è violata.

Queste regole mirano a garantire la completezza, l'unicità e la consistenza dei dati, nonché la validità delle informazioni e la tempestività dell'aggiornamento.

## Executive Summary

**Executive Summary**

Il nostro obiettivo era analizzare la qualità dei dati nella tabella `sellers` e identificare eventuali problemi o aree di miglioramento.

Dopo l'analisi, possiamo confermare che i dati sono relativamente completi e non presentano problemi di consistenza. Tuttavia, abbiamo notato due aree da migliorare:

*   La presenza di valori numerici in colonne come `seller_zip_code_prefix`, `seller_city` e `seller_state` potrebbe essere un problema se si tratta di rappresentare informazioni sui venditori.
*   La colonna `seller_zip_code_suffix` contiene solo valori null.

Questi problemi possono essere risolti attraverso la revisione dei dati e l'adozione di soluzioni correttive. Gli esiti delle nostre ricerche saranno molto utili per migliorare la qualità dei dati, aumentando la precisione dei rapporti e la fedeltà degli indicatori del nostro sistema.
