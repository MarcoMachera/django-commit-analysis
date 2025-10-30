# Guida Rapida all'Uso

## Progetto: Analisi Commit Django
**Automated Software Delivery - Università del Molise**

---

## File Principali

### Pre-analisi

Estrazione dei commit con:

```bash
cd django
git log --pretty=format:"%H;%an;%ad;%s" > ../commits.csv
cd ..
```

### Script Python

1. **`analisi_commit.py`** (PRINCIPALE)
   - Script di analisi di base
   - Identifica commit di refactoring/stile
   - Genera statistiche e grafici principali
   - **Comando:** `.venv/bin/python analisi_commit.py`

2. **`analisi_avanzate.py`**
   - Analisi approfondite (temporale, autori, keywords)
   - Genera grafici aggiuntivi
   - **Comando:** `.venv/bin/python analisi_avanzate.py`

---

## Installazione

### 1. Requisiti di Sistema
- Python 3.7 o superiore
- pip (gestore pacchetti Python)

### 2. Installazione Dipendenze

```bash
pip install -r requirements.txt
```

Oppure manualmente:
```bash
pip install pandas matplotlib
```

---

## Utilizzo

### Analisi Completa

```bash
# Passo 1: Analisi base
.venv/bin/python analisi_commit.py

# Passo 2: Analisi avanzate
.venv/bin/python analisi_avanzate.py
```

**Output totale:**
- Tutti i grafici (4 PNG)
- File CSV dei risultati

---

## File Generati

| File | Descrizione | Dimensione |
|------|-------------|------------|
| `grafico_commit.png` | Grafici principali (torta + barre) | ~267 KB |
| `analisi_temporale.png` | Evoluzione nel tempo | ~120 KB |
| `top_autori_refactoring.png` | Top 10 contributori | ~157 KB |
| `parole_chiave_frequenza.png` | Frequenza keywords | ~169 KB |
| `commit_refactoring.csv` | Commit identificati | ~323 KB |

---

## 📚 Documentazione

- **`README.md`** - Documentazione completa del progetto
- **`RIEPILOGO.md`** - Sintesi risultati e statistiche
- **Questo file** - Guida rapida all'uso

---

*Marco Machera - Ottobre 2025*
