#!/usr/bin/env python3
"""
Script di esempio per analisi avanzate sui commit di refactoring di Django
Automated Software Delivery - Marco Machera

"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import re


def analisi_temporale(csv_file='commit_refactoring.csv'):
    """
    Analizza l'evoluzione dei commit di refactoring nel tempo.
    """
    print("Analisi temporale dei commit di refactoring...")
    
    # Carica i dati
    df = pd.read_csv(csv_file, sep=';')
    
    # Converti le date in formato datetime (UTC per evitare warning)
    df['data_parsed'] = pd.to_datetime(df['data'], errors='coerce', utc=True)
    
    # Rimuovi righe con date non valide
    df = df.dropna(subset=['data_parsed'])
    
    # Estrai anno e mese
    df['anno'] = df['data_parsed'].dt.year
    df['anno_mese'] = df['data_parsed'].dt.to_period('M')
    
    # Conta commit per anno
    commit_per_anno = df.groupby('anno').size()
    
    print("\nCommit di refactoring per anno:")
    print(commit_per_anno.to_string())
    
    # Crea grafico temporale
    plt.figure(figsize=(12, 6))
    commit_per_anno.plot(kind='bar', color='#e74c3c', alpha=0.8, edgecolor='black')
    plt.title('Evoluzione Temporale dei Commit di Refactoring/Stile in Django', 
              fontsize=14, weight='bold', pad=20)
    plt.xlabel('Anno', fontsize=11, weight='bold')
    plt.ylabel('Numero di Commit', fontsize=11, weight='bold')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig('analisi_temporale.png', dpi=300, bbox_inches='tight')
    print("Grafico salvato: analisi_temporale.png")


def top_autori_refactoring(csv_file='commit_refactoring.csv', top_n=10):
    """
    Identifica gli autori più attivi nel refactoring.
    """
    print(f"\nTop {top_n} autori di commit di refactoring...")
    
    # Carica i dati
    df = pd.read_csv(csv_file, sep=';')
    
    # Conta commit per autore
    top_autori = df['autore'].value_counts().head(top_n)
    
    print(f"\nTop {top_n} contributori al refactoring:")
    for idx, (autore, count) in enumerate(top_autori.items(), 1):
        print(f"{idx:2d}. {autore:<30} - {count:3d} commit")
    
    # Crea grafico
    plt.figure(figsize=(12, 8))
    top_autori.plot(kind='barh', color='#3498db', alpha=0.8, edgecolor='black')
    plt.title(f'Top {top_n} Autori di Commit di Refactoring/Stile in Django', 
              fontsize=14, weight='bold', pad=20)
    plt.xlabel('Numero di Commit', fontsize=11, weight='bold')
    plt.ylabel('Autore', fontsize=11, weight='bold')
    plt.grid(axis='x', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig('top_autori_refactoring.png', dpi=300, bbox_inches='tight')
    print("Grafico salvato: top_autori_refactoring.png")


def analisi_parole_chiave(csv_file='commit_refactoring.csv'):
    """
    Analizza quali parole chiave sono più comuni nei commit di refactoring.
    """
    print("\nAnalisi delle parole chiave più comuni...")
    
    # Parole chiave da cercare
    parole_chiave = [
        'refactor', 'cleanup', 'style', 'pep8', 'lint', 
        'typo', 'naming', 'simplify', 'optimize', 'formatting',
        'cosmetic', 'whitespace', 'reorganize'
    ]
    
    # Carica i dati
    df = pd.read_csv(csv_file, sep=';')
    
    # Conta occorrenze di ogni parola chiave
    conteggi = {}
    for parola in parole_chiave:
        pattern = r'\b' + re.escape(parola) + r'\b'
        count = df['messaggio'].str.lower().str.contains(pattern, regex=True, na=False).sum()
        if count > 0:
            conteggi[parola] = count
    
    # Ordina per frequenza
    conteggi_ordinati = dict(sorted(conteggi.items(), key=lambda x: x[1], reverse=True))
    
    print("\nFrequenza delle parole chiave:")
    for parola, count in conteggi_ordinati.items():
        print(f"  {parola:<15} - {count:4d} occorrenze")
    
    # Crea grafico
    plt.figure(figsize=(12, 6))
    plt.bar(conteggi_ordinati.keys(), conteggi_ordinati.values(), 
            color='#9b59b6', alpha=0.8, edgecolor='black')
    plt.title('Frequenza delle Parole Chiave nei Commit di Refactoring', 
              fontsize=14, weight='bold', pad=20)
    plt.xlabel('Parola Chiave', fontsize=11, weight='bold')
    plt.ylabel('Numero di Occorrenze', fontsize=11, weight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig('parole_chiave_frequenza.png', dpi=300, bbox_inches='tight')
    print("Grafico salvato: parole_chiave_frequenza.png")


def statistiche_avanzate(csv_all='commits.csv', csv_ref='commit_refactoring.csv'):
    """
    Calcola statistiche avanzate confrontando commit normali e di refactoring.
    """
    print("\nStatistiche avanzate...")
    
    # Carica entrambi i dataset (gestisce meglio i caratteri ; nei messaggi)
    df_all = pd.read_csv(csv_all, sep=';', names=['hash', 'autore', 'data', 'messaggio'], 
                         on_bad_lines='skip')
    df_ref = pd.read_csv(csv_ref, sep=';', on_bad_lines='skip')
    
    # Lunghezza media dei messaggi
    df_all['lunghezza_msg'] = df_all['messaggio'].str.len()
    df_ref['lunghezza_msg'] = df_ref['messaggio'].str.len()
    
    media_normale = df_all[~df_all['hash'].isin(df_ref['hash'])]['lunghezza_msg'].mean()
    media_refactoring = df_ref['lunghezza_msg'].mean()
    
    print(f"\nLunghezza media messaggio:")
    print(f"  Commit normali:      {media_normale:.1f} caratteri")
    print(f"  Commit refactoring:  {media_refactoring:.1f} caratteri")
    print(f"  Differenza:          {media_refactoring - media_normale:+.1f} caratteri")
    
    # Numero di autori unici
    autori_totali = df_all['autore'].nunique()
    autori_refactoring = df_ref['autore'].nunique()
    
    print(f"\nAutori unici:")
    print(f"  Totali:              {autori_totali}")
    print(f"  Che fanno refactor:  {autori_refactoring}")
    print(f"  Percentuale:         {autori_refactoring/autori_totali*100:.1f}%")


def main():
    """
    Esegue tutte le analisi avanzate.
    """
    print("="*60)
    print("ANALISI AVANZATE - COMMIT REFACTORING DJANGO")
    print("="*60)
    
    try:
        # Verifica che i file esistano
        import os
        if not os.path.exists('commit_refactoring.csv'):
            print("Errore: Eseguire prima 'analisi_commit.py'")
            return
        
        # Esegue le analisi
        analisi_temporale()
        top_autori_refactoring()
        analisi_parole_chiave()
        statistiche_avanzate()
        
        print("\nAnalisi avanzate completate con successo!")
        
    except Exception as e:
        print(f"\nErrore: {e}")
        raise


if __name__ == "__main__":
    main()
