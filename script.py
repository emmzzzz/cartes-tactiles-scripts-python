# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 14:59:57 2025

@author: oulis
"""


import pandas as pd
import glob


fichiers = glob.glob("*.csv")
colonnes = ['Score', 'Classe', 'ID', 'Genre']  # Colonnes à garder


dfs = [pd.read_csv(f, skipinitialspace=True) for f in fichiers]
df_final = pd.concat(dfs, ignore_index=True)


if colonnes:
    colonnes_existantes = [c for c in colonnes if c in df_final.columns]
    df_final = df_final[colonnes_existantes]
    
# Ajouter colonne trial
df_final.insert(0, 'trial', ['T' + str(i+1) for i in range(len(df_final))])




# Sauvegarder le résultat
df_final.to_csv("resultat.csv", index=False)
