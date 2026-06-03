# DQ Audit - products

## Audit Tecnico

## Panoramica

La tabella `products` di Olist contiene informazioni relativi ai prodotti venduti sul marketplace. La struttura dei dati sembra essere coerente e ben definita, con otto colonne descrittive che descrivono le caratteristiche dei prodotti. La dimensione della tabella è piuttosto elevata, con oltre 32.000 righe.

## Problemi rilevati

Nonostante la struttura dei dati sembri essere coerente, ci sono alcuni aspetti che richiedono attenzione:

*   **Nullità dei dati**: le percentuali di nullità dei dati sono elevate in alcune colonne (1.9% per `product_category_name`, `product_name_lenght` e `product_description_lenght`). Ciò potrebbe indicare problemi nella raccolta o nella gestione dei dati.
*   **Duplicati**: non ci sono duplicati nei dati, il che è positivo ma non significa necessariamente che i dati siano completamente validi o coerenti.
*   **Statistiche numeriche**: le statistiche numeriche mostrano una buona distribuzione dei dati in alcune colonne (ad esempio `product_weight_g` e `product_length_cm`). Tuttavia, ci sono anche valori estremamente elevati o bassi che potrebbero essere indicativi di errori nella raccolta o nella gestione dei dati.

## Raccomandazioni

Per migliorare la qualità dei dati della tabella `products`, si possono implementare le seguenti strategie:

1.  **Verifica la correttezza dei dati**: controlla i dati per assicurarti che siano coerenti e validi. Ciò può essere fatto manualmente o utilizzando script di programmazione.
2.  **Aggiornamento delle colonne con nullità**: aggiorna le colonne con nullità dei dati per eliminarle e ottenere una distribuzione più uniforme.
3.  **Verifica la consistenza dei dati**: controlla i dati per assicurarti che siano coerenti tra loro e con gli altri dati della tabella.
4.  **Implementazione di controlli di data quality**: implementa controlli di data quality per prevenire l'inserimento di dati non validi o inconsistenti.

Seguendo queste raccomandazioni, potrete migliorare la qualità dei dati e ottenere una tabella più coerente e affidabile.

## Regole di Qualita

Ecco 7 regole di qualità dati formali per la tabella "products":

**REGOLA 1: ID prodotto univoco**
RULE_ID: RUP001
Colonna: product_id
Tipo: Unicità
Descrizione: Il valore nella colonna "product_id" deve essere unico e non può ripetersi.
Soglia: Nessun valore ripetuto

**REGOLA 2: Categorie di prodotto valide**
RULE_ID: RUP002
Colonna: product_category_name
Tipo: Validità
Descrizione: Il valore nella colonna "product_category_name" deve corrispondere a una categoria di prodotto valida.
Soglia: Nessun valore invalido (ad esempio, un valorino o una stringa vuota)

**REGOLA 3: Lunghezza del nome del prodotto**
RULE_ID: RUP003
Colonna: product_name_lenght
Tipo: Completa
Descrizione: Il valore nella colonna "product_name_lenght" deve essere compreso tra 2 e 50 (esclusi).
Soglia:
Minimo: 2
Massimo: 50

**REGOLA 4: Lunghezza della descrizione del prodotto**
RULE_ID: RUP004
Colonna: product_description_lenght
Tipo: Completa
Descrizione: Il valore nella colonna "product_description_lenght" deve essere compreso tra 10 e 200 (esclusi).
Soglia:
Minimo: 10
Massimo: 200

**REGOLA 5: Quantità di foto valida**
RULE_ID: RUP005
Colonna: product_photos_qty
Tipo: Completa
Descrizione: Il valore nella colonna "product_photos_qty" deve essere compreso tra 0 e 100 (esclusi).
Soglia:
Minimo: 0
Massimo: 100

**REGOLA 6: Peso del prodotto positivo**
RULE_ID: RUP006
Colonna: product_weight_g
Tipo: Completa
Descrizione: Il valore nella colonna "product_weight_g" deve essere positivo.
Soglia:
Minimo: 0

**REGOLA 7: Dimensioni del prodotto valide**
RULE_ID: RUP007
Colonne: product_length_cm, product_height_cm, product_width_cm
Tipo: Consistenza
Descrizione: Il valore nella colonna "product_length_cm" deve essere maggiore di 0 e minore o uguale alla dimensione della colonna "product_width_cm".
Soglia:
Length cm > 0 AND Length cm <= Width cm

Queste regole possono aiutare a garantire la qualità dei dati nella tabella "products" e prevenire errori di input.

## Executive Summary

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
