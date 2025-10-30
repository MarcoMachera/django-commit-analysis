# 📊 Riepilogo Analisi Commit Django

## Progetto: Automated Software Delivery
**Università del Molise - Prof. Simone Scalabrino**  
**Studente:** Marco Machera  
**Data:** 30 ottobre 2025

---

## 🎯 Domanda di Ricerca

> **"Quanti commit hanno migliorato lo stile del codice o hanno effettuato operazioni di refactoring?"**

---

## 📈 Risultati Principali

### Analisi di Base

| Metrica | Valore | Percentuale |
|---------|--------|-------------|
| **Totale commit analizzati** | 33,567 | 100% |
| **Commit di refactoring/stile** | 2,115 | **6.30%** |
| **Commit normali** | 31,452 | 93.70% |

### Insight Chiave

✅ **Circa 1 commit su 16 è dedicato al refactoring/stile**

✅ **Django dimostra un forte impegno per la qualità del codice**

✅ **Il refactoring è una pratica costante, non sporadica**

---

## 🔍 Analisi Temporale

### Distribuzione per Anno (2005-2025)

Gli anni con più commit di refactoring:
1. **2008** - 205 commit
2. **2007** - 178 commit
3. **2013** - 166 commit
4. **2014** - 164 commit
5. **2010** - 155 commit

### Osservazioni

- **Picco tra 2007-2008**: Periodo di crescita e maturazione del framework
- **Costante attenzione**: Anche negli anni recenti (2024-2025) si mantiene intorno a 50 commit/anno
- **Stabilità**: Il progetto mantiene pratiche di refactoring costanti nel tempo

---

## 👥 Top Contributori al Refactoring

| Posizione | Autore | Commit Refactoring |
|-----------|--------|-------------------|
| 🥇 1 | Adrian Holovaty | 263 |
| 🥈 2 | Tim Graham | 198 |
| 🥉 3 | Russell Keith-Magee | 150 |
| 4 | Malcolm Tredinnick | 141 |
| 5 | Mariusz Felisiak | 75 |
| 6 | Aymeric Augustin | 66 |
| 7 | Gary Wilson Jr | 62 |
| 8 | Alex Gaynor | 56 |
| 9 | Jannis Leidel | 48 |
| 10 | James Bennett | 43 |

### Insight

- **Adrian Holovaty** (co-fondatore di Django) ha il maggior numero di commit di refactoring
- I **core maintainer** sono i principali contributori al refactoring
- **479 autori su 3,155 (15.2%)** hanno fatto almeno un commit di refactoring

---

## 🔤 Parole Chiave Più Frequenti

| Parola Chiave | Occorrenze | Descrizione |
|---------------|------------|-------------|
| **typo** | 1,326 | Correzione errori di battitura |
| **formatting** | 196 | Miglioramenti formattazione |
| **style** | 173 | Miglioramenti stile codice |
| **cleanup** | 94 | Pulizia codice |
| **whitespace** | 71 | Correzioni spazi bianchi |
| **cosmetic** | 50 | Modifiche estetiche |
| **pep8** | 40 | Conformità PEP 8 |
| **naming** | 33 | Miglioramenti naming |
| **refactor** | 29 | Refactoring esplicito |

### Osservazioni

- **La maggior parte dei commit (1,326)** corregge errori di battitura (typo)
- **Forte attenzione alla formattazione** (196 + 71 commit)
- **PEP 8** è esplicitamente menzionato in 40 commit
- **Il termine "refactor"** è usato esplicitamente solo 29 volte (molto specifico)

---

## 📊 Statistiche Comparative

### Lunghezza Media Messaggi

| Tipo Commit | Lunghezza Media |
|-------------|-----------------|
| Commit normali | 76.4 caratteri |
| Commit refactoring | 63.9 caratteri |
| **Differenza** | **-12.5 caratteri** |

**Insight**: I commit di refactoring tendono ad avere messaggi più brevi e concisi.

### Partecipazione degli Autori

| Metrica | Valore |
|---------|--------|
| Autori totali | 3,155 |
| Autori che fanno refactoring | 479 |
| **Percentuale** | **15.2%** |

**Insight**: Solo il 15% degli autori contribuisce al refactoring, suggerendo che è un'attività più specializzata.

---

## 🎓 Conclusioni per il Progetto

### Risposta alla Domanda di Ricerca

**Il 6.30% dei commit di Django (2,115 su 33,567) sono dedicati al refactoring o al miglioramento dello stile del codice.**

### Implicazioni

1. **Qualità del Codice**: Django mantiene un focus costante sulla qualità
2. **Best Practice**: Il refactoring è integrato nel processo di sviluppo
3. **Sostenibilità**: L'attenzione continua al refactoring contribuisce alla longevità del progetto
4. **Community**: Un sottogruppo specializzato di contributori si occupa del refactoring

### Limitazioni dello Studio

- **Analisi basata su keywords**: Potrebbero esserci falsi positivi/negativi
- **Solo messaggi di commit**: Non analizza il contenuto effettivo del codice
- **Soggettività**: La classificazione dipende dalla terminologia usata dagli autori
- **Lingua inglese**: Assume messaggi in inglese

### Possibili Estensioni Future

1. Analisi del diff del codice (metriche di complessità)
2. Machine Learning per classificazione automatica
3. Correlazione tra refactoring e bug fixing
4. Analisi per modulo/componente di Django
5. Studio dell'impatto del refactoring sulla qualità

---

## 📁 File Generati

### Script Python
- ✅ `analisi_commit.py` - Script principale di analisi
- ✅ `analisi_avanzate.py` - Analisi approfondite

### Dati
- ✅ `commits.csv` - Dataset completo (33,567 commit)
- ✅ `commit_refactoring.csv` - Commit di refactoring (2,115)

### Visualizzazioni
- ✅ `grafico_commit.png` - Torta + barre (base)
- ✅ `analisi_temporale.png` - Evoluzione nel tempo
- ✅ `top_autori_refactoring.png` - Top 10 contributori
- ✅ `parole_chiave_frequenza.png` - Frequenza keywords

### Documentazione
- ✅ `README.md` - Documentazione completa
- ✅ `RIEPILOGO.md` - Questo documento
- ✅ `requirements.txt` - Dipendenze Python

---

## 🛠️ Tecnologie Utilizzate

- **Python 3.13**: Linguaggio di programmazione
- **pandas 2.x**: Analisi e manipolazione dati
- **matplotlib 3.x**: Visualizzazione grafici
- **Git**: Estrazione dati repository

---

## 💡 Metodologia

1. **Estrazione dati**: `git log` da repository Django
2. **Preprocessing**: Caricamento e pulizia con pandas
3. **Classificazione**: Pattern matching con regex su keywords
4. **Analisi**: Calcolo statistiche aggregate
5. **Visualizzazione**: Grafici con matplotlib
6. **Validazione**: Verifica manuale campioni

---

**Marco Machera**  
*Automated Software Delivery*  
*Università del Molise*  
*Ottobre 2025*
