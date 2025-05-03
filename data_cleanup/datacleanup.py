import pandas as pd
from tabulate import tabulate 
import numpy as np

#Bereinigung der Tabelle ab_ag.tsv
# TSV Datei laden (mit absolutem path)
df = pd.read_csv("/Users/annika/Downloads/ab_ag.tsv", sep="\t")


# 1. Übersicht über Spalten 

# Berechnung Anzahl NA pro Spalte 
na_counts = df.isna().sum()
# Ausgabe NA-Anzahl
print("Anzahl fehlender Werte pro Spalte:")
print(na_counts)

#Berechnung Prozent NA pro Spalte 
na_percent = (na_counts / len(df)) * 100
print("Prozentanzahl NA pro Spalte:")
print(na_percent)




#2. Löschen von NA-Spalten 

# Umwandlung None in NA 

df = df.replace({None: np.nan})

# Löschung erfolgt nur wenn mind. 85% NA
min_non_na_ratio = 0.15

# Berechnung absolute Mindestzahl NA
min_non_na_count = int(len(df) * min_non_na_ratio)

# Spalten über dem Wert löschen 
df_clean = df.dropna(axis=1, thresh=min_non_na_count)

# Speichern als neue .tsv Datei 
df_clean.to_csv("bereinigt.tsv", sep="\t", index=False)

# Ausgabe in Terminal 
print(df_clean)


#3. Überischt Tabelle df_clean.tsv erstellen

# Als Markdown-Tabelle exportieren
with open("df_clean.tsv", "w") as f:
    f.write(tabulate(df_clean, headers='keys', tablefmt='github'))
