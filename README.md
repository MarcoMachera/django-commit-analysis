# Analisi Commit Django - Automated Software Delivery

**Università del Molise**  
**Corso:** Automated Software Delivery  
**Docente:** Prof. Simone Scalabrino  
**Studente:** Marco Machera  
**Data:** 30 ottobre 2025

---

## 📋 Obiettivo del Progetto

Questo progetto analizza la storia dei commit del repository Django (https://github.com/django/django) per rispondere alla seguente domanda di ricerca:

> **"Quanti commit hanno migliorato lo stile del codice o hanno effettuato operazioni di refactoring?"**

---

## 📊 Risultati dell'Analisi

### Statistiche Principali

- **Totale commit analizzati:** 33,567
- **Commit di refactoring/stile:** 2,115 (6.30%)
- **Commit normali:** 31,452 (93.70%)

### Interpretazione

I risultati mostrano che circa il **6.30%** dei commit nel repository Django sono dedicati a operazioni di refactoring o miglioramento dello stile del codice. Questo indica che:

1. Django mantiene un focus costante sulla qualità del codice
2. Circa 1 commit su 16 è dedicato al miglioramento della base di codice esistente
3. Il team Django investe tempo significativo nella manutenzione e pulizia del codice

---

## 🛠️ Metodologia

### 1. Estrazione dei Commit

I commit sono stati estratti dal repository Django utilizzando il comando Git:

```bash
git log --pretty=format:"%H;%an;%ad;%s" > commits.csv
```

Questo comando produce un file CSV con le seguenti colonne:
- **Hash:** Identificatore univoco del commit
- **Autore:** Nome dell'autore del commit
- **Data:** Data e ora del commit
- **Messaggio:** Messaggio descrittivo del commit

### 2. Identificazione dei Commit di Refactoring

Lo script identifica i commit di refactoring cercando le seguenti parole chiave nel messaggio del commit:

- `refactor`
- `cleanup` / `clean up`
- `reformat`
- `style`
- `pep8` / `pep 8`
- `lint`
- `typo`
- `naming`
- `readability`
- `dead code`
- `simplify`
- `optimize`
- `formatting`
- `reorganize`
- `restructure`
- `cosmetic`
- `whitespace`
- `indentation`
- `code style`
- `code quality`
- `improve code`

La ricerca è **case-insensitive** e utilizza **word boundaries** per evitare falsi positivi.

### 3. Analisi e Visualizzazione

Lo script:
1. Carica i commit dal file CSV
2. Analizza ogni messaggio di commit
3. Classifica i commit come "refactoring/stile" o "normali"
4. Calcola statistiche aggregate
5. Genera visualizzazioni grafiche (torta e barre)
6. Salva i risultati in file di output

---

## 📁 Struttura del Progetto

```
Automated Software delivery/
│
├── analisi_commit.py          # Script principale di analisi
├── commits.csv                # Dati di input (commit estratti)
├── grafico_commit.png         # Grafico generato (output)
├── commit_refactoring.csv     # Commit di refactoring identificati (output)
└── README.md                  # Questa documentazione
```

---

## 🚀 Installazione e Utilizzo

### Prerequisiti

- Python 3.7 o superiore
- pip (gestore pacchetti Python)

### Installazione Dipendenze

```bash
pip install pandas matplotlib
```

### Esecuzione dello Script

```bash
python3 analisi_commit.py
```

### Output Generati

1. **Output a console:** Statistiche dettagliate e esempi di commit
2. **grafico_commit.png:** Visualizzazioni grafiche (torta e barre)
3. **commit_refactoring.csv:** Lista completa dei commit identificati come refactoring

---

## 📈 Visualizzazioni

Il grafico generato include:

1. **Grafico a torta:** Mostra la proporzione tra commit normali e di refactoring/stile
2. **Grafico a barre:** Confronto visivo del numero di commit per categoria

---

## 🔍 Esempi di Commit Identificati

Ecco alcuni esempi di commit classificati come refactoring/stile:

1. **Hash:** 42d6e20feb  
   **Messaggio:** "Made cosmetic edits to docs/releases/6.0.txt."

2. **Hash:** a545eb0c1a  
   **Messaggio:** "Cautioned against multi-level relative imports in coding style docs."

3. **Hash:** 6c82b0bc91  
   **Messaggio:** "Made cosmetic edits to 5.2.7 release notes."

4. **Hash:** 7528979153  
   **Messaggio:** "Added cleanup of cache clearing to DjangoFilePrefixesTests.setUp()."

---

## 💡 Considerazioni Tecniche

### Vantaggi dell'Approccio

- **Automatizzato:** Analisi rapida di decine di migliaia di commit
- **Riproducibile:** Lo script può essere eseguito su qualsiasi repository
- **Estensibile:** Facile aggiungere nuove parole chiave o metriche
- **Visuale:** Grafici chiari per presentazioni

### Limitazioni

- **Keyword-based:** L'analisi si basa solo sui messaggi dei commit
- **Falsi positivi/negativi:** Alcuni commit potrebbero essere mal classificati
- **Lingua:** Assume messaggi in inglese
- **Contenuto:** Non analizza il contenuto effettivo del codice modificato

### Possibili Miglioramenti Futuri

1. Analisi del diff del codice (non solo il messaggio)
2. Machine Learning per classificazione più accurata
3. Analisi temporale (trend nel tempo)
4. Analisi per autore o file
5. Integrazione con tool di analisi statica del codice

---

## 📚 Riferimenti

- **Repository Django:** https://github.com/django/django
- **Corso:** Automated Software Delivery - Università del Molise
- **Documentazione Git:** https://git-scm.com/docs/git-log

---

Il progetto fornisce insight quantitativi sulla qualità del processo di sviluppo di Django, uno dei framework web più popolari al mondo.

---

**Marco Machera**  
*Automated Software Delivery - Università del Molise*  
*Ottobre 2025*
