# DQ Audit - geolocation

## Audit Tecnico

**Analisi della qualità dei dati di Olist - Geolocation**

La tabella `geolocation` contiene informazioni geografiche su utenti e imprese presenti su Olist, con un totale di 1.000.163 righe. In questo rapporto, analizzeremo la qualità dei dati esistenti nella tabella.

### Problemi rilevati

#### Duplicati
Il numero elevato di duplicati (261831) indica una carenza di identificazione univoca per ogni riga. Questo potrebbe essere dovuto a diverse fonti che inviano le stesse informazioni, senza la presenza di un id univoco.

#### Codici zip prefix invalidi
Il range dei codici zip prefix (1001.00 - 99990.00) sembra troppo ampio e non corrisponde ai standard Brasiliani. Alcuni valori di zip sono anche fuori da questo range.

#### Coordinate geografiche incomplete o errorate
Le coordinate latitudine e longitudinale sono presenti in modo errato o incompleto, con valori estremamente lontani dalla normalità (min/max).

### Raccomandazioni

1.  **Creazione di un id univoco**: Utilizzare una funzione hash o generatore univoco per ogni riga della tabella `geolocation`, in modo da poter identificare le duplicazioni e assicurarsi che ogni riga sia trattata come unica entità.
2.  **Verifica dei codici zip prefix**: Valutare i valori dei codici zip prefix e aggiornarli ai standard Brasiliani, eliminando eventuali valori invalidi.
3.  **Ottimizzazione delle coordinate geografiche**: Utilizzare una funzione di ottimizzazione per correggere le coordinate latitudine e longitudinale, garantendo che siano presenti in modo coerente e completo.

**Riepilogo**

La tabella `geolocation` contiene dati importanti ma con alcuni problemi significativi, come duplicati e errori nella rappresentazione delle coordinate geografiche. Per migliorare la qualità dei dati è necessario implementare alcune raccomandazioni per ottimizzare i dati.

## Regole di Qualita

Ecco 7 regole di qualità dati formali per la tabella "geolocation":

**RULE_1**: geolocation_zip_code_prefix, Tipo (Completezza), Descrizione: Deve contenere solo caratteri numerici e lettere (A-Z). Soglia: 0.9

La regola richiede che il campo "geolocation_zip_code_prefix" non contenga caratteri speciali o simboli non alfabetici, ma solo lettere maiuscole e numeri.

**RULE_2**: geolocation_lat, Tipo (Completezza), Descrizione: Deve contenere un numero reale compreso tra -90 e 90. Soglia: 0.95

La regola richiede che il campo "geolocation_lat" sia un numero reale che rappresenta una latitudine geografica valida.

**RULE_3**: geolocation_lng, Tipo (Completezza), Descrizione: Deve contenere un numero reale compreso tra -180 e 180. Soglia: 0.95

La regola richiede che il campo "geolocation_lng" sia un numero reale che rappresenta una longitudine geografica valida.

**RULE_4**: geolocation_city, Tipo (Completezza), Descrizione: Deve contenere solo caratteri alfabetici e spazi. Soglia: 0.85

La regola richiede che il campo "geolocation_city" non contenga caratteri speciali o simboli non alfabetici, ma solo lettere maiuscole e minuscole.

**RULE_5**: geolocation_state, Tipo (Completezza), Descrizione: Deve contenere solo caratteri alfabetici e spazi. Soglia: 0.85

La regola richiede che il campo "geolocation_state" non contenga caratteri speciali o simboli non alfabetici, ma solo lettere maiuscole e minuscole.

**RULE_6**: geolocation_zip_code_prefix, Tipo (Unicita), Descrizione: Non può essere ripetuto. Soglia: 0.99

La regola richiede che il campo "geolocation_zip_code_prefix" non possa contenere più di un valore unico.

**RULE_7**: geolocation_lat, geolocation_lng, Tipo (Consistenza), Descrizione: Non possono essere null contemporaneamente. Soglia: 0.98

La regola richiede che almeno una delle colonne "geolocation_lat" e "geolocation_lng" non possa essere null contemporaneamente.

## Executive Summary

**Executive Summary: Analisi della qualità dei dati di Olist - Geolocation**

Il nostro rapporto analizza la tabella `geolocation` contenente informazioni geografiche su utenti e imprese presenti su Olist. Gli esiti del nostro lavoro mostrano alcune preoccupazioni sulla qualità dei dati presenti nella tabella:

*   La presenza di duplicati (261831) suggerisce una mancanza di identificazione univoca per ogni riga, potenzialmente dovuta a diverse fonti che inviano le stesse informazioni senza un id univoco.
*   Il codice zip prefix ha un range troppo ampio e non corrisponde ai standard Brasiliani, con alcuni valori fuori da questo range.
*   Le coordinate geografiche sono incomplete o errorate, compromettendo l'accuratezza delle informazioni.

Questi problemi possono avere impatti significativi sulla nostra comprensione dei dati e sulla qualità del servizio offerto a nossi utenti. Saremo in grado di esplorare soluzioni per risolvere questi problemi e migliorare la qualità dei dati.
