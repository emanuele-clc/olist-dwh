# L3 - Cleaning: geolocation

**Data:** 2026-05-09 12:01 | **Provider:** ollama

## Piano di Cleaning

```json
{
  "table": "geolocation",
  "steps": [
    {
      "step_id": 1,
      "name": "Eliminazione duplicati",
      "description": "Rimuovere le righe duplicati per il codice prefisso della posizione geografica",
      "columns": [],
      "pandas_method": "drop_duplicates(subset=['geolocation_zip_code_prefix'], keep='first', inplace=True)",
      "priority": "high",
      "business_impact": "Eliminare le duplicate può influenzare la precisione dei risultati"
    },
    {
      "step_id": 2,
      "name": "Crittografia zip code prefix",
      "description": "Criptografare il codice prefisso della posizione geografica per proteggere i dati sensibili",
      "columns": [],
      "pandas_method": "geopandas.utils.crispify_column('geolocation_zip_code_prefix')",
      "priority": "medium",
      "business_impact": "La crittografia è importante per proteggere i dati sensibili"
    },
    {
      "step_id": 3,
      "name": "Normale scale delle coordinate",
      "description": "Normare la scala delle coordinate latitudinari e longitudinarie",
      "columns": [],
      "pandas_method": [
        "geopandas.utils.scale_column('geolocation_lat', 'min=-36.61, max=45.07')",
        "geopandas.utils.scale_column('geolocation_lng', 'min=-101.47, max=121.11')"
      ],
      "priority": "low",
      "business_impact": "La normalizzazione delle coordinate non influenza direttamente i risultati"
    }
  ]
}
```

## Narrativa Audit

**Audit sulla Tabella Olist "geolocation" - Risultati e Impatti**

L'analisi dei dati pre- e post-cleaning della tabella Olist "geolocation" ha rivelato una serie di trasformazioni significative che hanno migliorato la qualità e la precisione delle informazioni. Questo report sintetizza gli risultati dell'audit, evidenziando le principali trasformazioni, impatti sulla qualità, limitazioni e raccomandazioni per future migliorie.

**Sintesi dell'intervento**

L'intervento di cleaning della tabella Olist "geolocation" ha seguito un percorso di deduplicatione, standardizzazione e geo-aggregazione per migliorare la qualità delle informazioni. Il processo è stato suddiviso in tre fasi principali:

1. Deduplicatione: rimozione dei duplicati identificati tramite l'uso del primary key.
2. Standardizzazione: normalizzazione dei dati relativi alla città e allo stato per aumentare la precisione delle informazioni.
3. Geo-aggregazione per ZIP: filtro dei dati per escludere coordinate fuori dall'emissario Brasile e calcolo della media latitudine e longitudine per ogni zip.

**Trasformazioni principali**

* Riduzione del numero di duplicati da 261831 a 0
* Aggiunta di una nuova colonna "n_records" con il conteggio delle registrazioni dopo la cleaning
* Aumento del numero di righe dalla 1000163 alla 19010

**Impatto sulla qualità**

L'intervento di cleaning ha avuto un impatto significativo sulla qualità delle informazioni, rendendo più precise e complete le coordinate geografiche. La riduzione dei duplicati è stata particolarmente utile per diminuire l'errore e aumentare la affidabilità dei dati.

**Limitazioni**

* L'intervento non ha considerato tutte le possibili varianti delle coordinate geografiche, potenzialmente escludendo alcune informazioni importanti.
* La geo-aggregazione per ZIP ha richiesto una riduzione del numero di righe, potenzialmente alterando la relazione temporale tra le diverse registrazioni.

**Raccomandazioni**

* Implementare un sistema di verifica e controllo più rigoroso per garantire l'omogeneità delle coordinate geografiche.
* Utilizzare tecniche di learning machine o clustering per rilevare eventuali pattern o anomalie nella distribuzione delle coordinate geografiche.
* Considerare l'utilizzo di fonti aggiornate e accurate per la geo-aggregazione, ad esempio tramite il uso di dataset pubblici o collaborazioni con enti locali.

In sintesi, l'intervento di cleaning della tabella Olist "geolocation" ha rivelato una serie di trasformazioni significative che hanno migliorato la qualità e la precisione delle informazioni. Tuttavia, è importante considerare le limitazioni e le raccomandazioni per future migliorie e implementazione di sistemi più rigorosi e efficaci.
