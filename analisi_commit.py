#!/usr/bin/env python3
"""
Script per l'analisi dei commit di Django - Progetto Automated Software Delivery
Università del Molise - Marco Machera

Obiettivo: Identificare quanti commit hanno migliorato lo stile del codice 
o hanno effettuato operazioni di refactoring.

Autore: Marco Machera
Data: 30 ottobre 2025
"""

import pandas as pd
import matplotlib.pyplot as plt
import re
from typing import Tuple, List


# ============================================================================
# CONFIGURAZIONE PAROLE CHIAVE
# ============================================================================

# Parole chiave che indicano refactoring o miglioramento dello stile
PAROLE_CHIAVE_REFACTORING = [
    'refactor',
    'cleanup',
    'clean up',
    'reformat',
    'style',
    'pep8',
    'pep 8',
    'lint',
    'typo',
    'naming',
    'readability',
    'dead code',
    'simplify',
    'optimize',
    'formatting',
    'reorganize',
    'restructure',
    'cosmetic',
    'whitespace',
    'indentation',
    'code style',
    'code quality',
    'improve code',
]


# ============================================================================
# FUNZIONI PRINCIPALI
# ============================================================================

def carica_commit(percorso_file: str) -> pd.DataFrame:
    """
    Carica il file CSV contenente i commit di Django.
    
    Args:
        percorso_file: Percorso del file CSV con i commit
        
    Returns:
        DataFrame pandas con i dati dei commit
    """
    print(f"Caricamento file: {percorso_file}")
    
    try:
        # Legge il CSV usando ; come separatore
        df = pd.read_csv(
            percorso_file,
            sep=';',
            names=['hash', 'autore', 'data', 'messaggio'],
            encoding='utf-8',
            on_bad_lines='skip'  # Ignora righe malformate
        )
        
        print(f"File caricato con successo: {len(df)} commit trovati")
        return df
        
    except FileNotFoundError:
        print(f"Errore: File {percorso_file} non trovato!")
        raise
    except Exception as e:
        print(f"Errore durante il caricamento: {e}")
        raise


def è_commit_refactoring(messaggio: str, parole_chiave: List[str]) -> bool:
    """
    Determina se un messaggio di commit indica un'operazione di refactoring
    o miglioramento dello stile.
    
    Args:
        messaggio: Messaggio del commit da analizzare
        parole_chiave: Lista di parole chiave da cercare
        
    Returns:
        True se il commit è di refactoring/stile, False altrimenti
    """
    if pd.isna(messaggio):
        return False
    
    # Converte il messaggio in minuscolo per il confronto case-insensitive
    messaggio_lower = messaggio.lower()
    
    # Verifica se almeno una parola chiave è presente nel messaggio
    for parola in parole_chiave:
        # Usa word boundary (\b) per evitare match parziali
        # es. "refactor" non deve matchare "refactory"
        pattern = r'\b' + re.escape(parola) + r'\b'
        if re.search(pattern, messaggio_lower):
            return True
    
    return False


def analizza_commit(df: pd.DataFrame, parole_chiave: List[str]) -> Tuple[pd.DataFrame, dict]:
    """
    Analizza i commit e identifica quelli relativi a refactoring/stile.
    
    Args:
        df: DataFrame con i commit
        parole_chiave: Lista di parole chiave per identificare refactoring
        
    Returns:
        Tupla contenente:
        - DataFrame con colonna aggiuntiva 'è_refactoring'
        - Dizionario con le statistiche dell'analisi
    """
    
    # Applica la funzione di controllo a ogni messaggio
    df['è_refactoring'] = df['messaggio'].apply(
        lambda msg: è_commit_refactoring(msg, parole_chiave)
    )
    
    # Calcola statistiche
    totale_commit = len(df)
    commit_refactoring = df['è_refactoring'].sum()
    percentuale = (commit_refactoring / totale_commit * 100) if totale_commit > 0 else 0
    
    statistiche = {
        'totale': totale_commit,
        'refactoring': commit_refactoring,
        'normali': totale_commit - commit_refactoring,
        'percentuale': percentuale
    }
    
    print("Analisi completata!")
    
    return df, statistiche


def stampa_risultati(statistiche: dict):
    """
    Stampa i risultati dell'analisi in formato leggibile.
    
    Args:
        statistiche: Dizionario con le statistiche calcolate
    """
    print("\n" + "="*60)
    print("RISULTATI DELL'ANALISI")
    print("="*60)
    print(f"Totale commit analizzati: {statistiche['totale']:,}")
    print(f"Commit di refactoring/stile: {statistiche['refactoring']:,} ({statistiche['percentuale']:.2f}%)")
    print(f"Commit normali: {statistiche['normali']:,} ({100-statistiche['percentuale']:.2f}%)")
    print("="*60)


def genera_grafico(statistiche: dict, percorso_output: str = 'grafico_commit.png'):
    """
    Genera e salva visualizzazioni grafiche dei risultati.
    
    Args:
        statistiche: Dizionario con le statistiche calcolate
        percorso_output: Percorso dove salvare il grafico
    """
    print(f"\nGenerazione grafici...")
    
    # Crea una figura con due subplot: torta e barre
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # --- GRAFICO A TORTA ---
    labels = ['Commit normali', 'Refactoring/Stile']
    sizes = [statistiche['normali'], statistiche['refactoring']]
    colors = ['#3498db', '#e74c3c']
    explode = (0, 0.1)  # "Esplode" la fetta del refactoring
    
    ax1.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct='%1.2f%%',
        shadow=True,
        startangle=90,
        textprops={'fontsize': 11, 'weight': 'bold'}
    )
    ax1.set_title('Distribuzione Commit Django\n(Normali vs Refactoring/Stile)', 
                  fontsize=13, weight='bold', pad=20)
    
    # --- GRAFICO A BARRE ---
    categorie = ['Commit\nnormali', 'Refactoring/\nStile']
    valori = [statistiche['normali'], statistiche['refactoring']]
    
    bars = ax2.bar(categorie, valori, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    # Aggiunge etichette con i valori sopra le barre
    for bar, valore in zip(bars, valori):
        height = bar.get_height()
        ax2.text(
            bar.get_x() + bar.get_width()/2.,
            height,
            f'{valore:,}\n({valore/statistiche["totale"]*100:.2f}%)',
            ha='center',
            va='bottom',
            fontsize=11,
            weight='bold'
        )
    
    ax2.set_ylabel('Numero di commit', fontsize=11, weight='bold')
    ax2.set_title(f'Confronto Commit Django\n(Totale: {statistiche["totale"]:,} commit)', 
                  fontsize=13, weight='bold', pad=20)
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Formattazione asse Y con separatore migliaia
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))
    
    # Aggiunge informazioni generali
    fig.suptitle('Analisi Commit Django - Automated Software Delivery\nMarco Machera - Università del Molise', 
                 fontsize=14, weight='bold', y=1.02)
    
    plt.tight_layout()
    
    # Salva il grafico
    plt.savefig(percorso_output, dpi=300, bbox_inches='tight')
    print(f"Grafico salvato: {percorso_output}")


def mostra_esempi_commit(df: pd.DataFrame, n_esempi: int = 5):
    """
    Mostra alcuni esempi di commit identificati come refactoring.
    
    Args:
        df: DataFrame con i commit analizzati
        n_esempi: Numero di esempi da mostrare
    """
    commit_ref = df[df['è_refactoring'] == True]
    
    if len(commit_ref) == 0:
        print("\nNessun commit di refactoring trovato.")
        return
    
    print(f"\nEsempi di commit di refactoring/stile (primi {n_esempi}):")
    print("-" * 80)
    
    for idx, row in commit_ref.head(n_esempi).iterrows():
        print(f"\n Hash: {row['hash'][:10]}")
        print(f"   Autore: {row['autore']}")
        print(f"   Data: {row['data']}")
        print(f"   Messaggio: {row['messaggio'][:100]}...")


# ============================================================================
# FUNZIONE PRINCIPALE
# ============================================================================

def main():
    """
    Funzione principale che orchestra l'intera analisi.
    """
    print("\n" + "="*60)
    print("🎓 ANALISI COMMIT DJANGO - AUTOMATED SOFTWARE DELIVERY")
    print("   Università del Molise - Marco Machera")
    print("="*60)
    
    # Percorso del file CSV
    PERCORSO_CSV = 'commits.csv'
    PERCORSO_GRAFICO = 'grafico_commit.png'
    
    try:
        # 1. Carica i commit dal file CSV
        df = carica_commit(PERCORSO_CSV)
        
        # 2. Analizza i commit
        df_analizzato, statistiche = analizza_commit(df, PAROLE_CHIAVE_REFACTORING)
        
        # 3. Stampa i risultati
        stampa_risultati(statistiche)
        
        # 4. Mostra esempi di commit
        mostra_esempi_commit(df_analizzato, n_esempi=5)
        
        # 5. Genera il grafico
        genera_grafico(statistiche, PERCORSO_GRAFICO)
        
        # 6. Salva risultati in un file CSV (opzionale)
        output_csv = 'commit_refactoring.csv'
        df_refactoring = df_analizzato[df_analizzato['è_refactoring'] == True]
        df_refactoring.to_csv(output_csv, index=False, sep=';', encoding='utf-8')
        print(f"Commit di refactoring salvati in: {output_csv}")
        
        print("\nAnalisi completata con successo!")
        
    except Exception as e:
        print(f"\nErrore durante l'esecuzione: {e}")
        raise


# ============================================================================
# PUNTO DI INGRESSO
# ============================================================================

if __name__ == "__main__":
    main()
