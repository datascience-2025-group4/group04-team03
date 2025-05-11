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
df_clean1 = df.dropna(axis=1, thresh=min_non_na_count)

# Speichern als neue .tsv Datei 
df_clean1.to_csv("bereinigt.tsv", sep="\t", index=False)



# zu löschende Spalten benennen
zu_loeschende_spalten = ["authors", "date"]

# Löscheen der Spalten
df_clean = df_clean1.drop(columns=[spalte for spalte in zu_loeschende_spalten if spalte in df_clean1.columns])

# Ausgabe in Terminal 
print(df_clean)


#3. Überischt Tabelle df_clean.tsv erstellen

# Als Markdown-Tabelle exportieren
with open("df_clean.tsv", "w") as f:
    f.write(tabulate(df_clean, headers='keys', tablefmt='github'))



#Vergleichen der uniprot data und ab_ag.tsv

# Einlesen der Dateien (Passe Pfade/Spaltennamen ggf. an)
df1 = pd.read_csv("data/uniprot_data.tsv", sep="\t")
df2 = pd.read_csv("data/ab_ag.tsv", sep="\t")
#Vereinheitlichung der Spaltennamen 
df1 = df1.rename(columns={"From": "pdb"})
df1["pdb"] = df1["pdb"].str.lower().str.strip()
# Standardisieren der PDB-ID-Spalte (z. B. alles klein, keine Leerzeichen)
df1["pdb"] = df1["pdb"].str.lower().str.strip()
df2["pdb"] = df2["pdb"].str.lower().str.strip()
# Nur eindeutige PDB-Einträge behalten
df1_unique = df1.drop_duplicates(subset="pdb")
df2_unique = df2.drop_duplicates(subset="pdb")
# Vergleich der PDB-Codes als Mengen
pdb_df1 = set(df1_unique["pdb"])
pdb_df2 = set(df2_unique["pdb"])
gemeinsame = pdb_df1 & pdb_df2
nur_in_df1 = pdb_df1 - pdb_df2
nur_in_df2 = pdb_df2 - pdb_df1
# Ausgabe
print("Gemeinsame PDB-Codes:", len(gemeinsame))
print("Nur in UniProt:", len(nur_in_df1))
print("Nur in ab_ag_tsv:", len(nur_in_df2))
#Überprüfung der Anzahl an nicht doppelten Einträgen in ab_ag.tsv
anzahl_eindeutiger_pdb_df2 = df2["pdb"].drop_duplicates().shape[0]
print("Eindeutige PDB-Einträge in df2:", anzahl_eindeutiger_pdb_df2)




# wieviele verscheidene Methods hat ab_ag.tsv ? 
anzahl_methoden = df2["method"].nunique()
print("Anzahl unterschiedlicher Methoden:", anzahl_methoden)
unique_methods = df2["method"].dropna().unique()
for method in unique_methods:
    print(method)
#wie oft kommen die einzenlen Methods vor ? 
method_counts = df2["method"].value_counts(dropna=False)
print(method_counts)



#Quantifikation der verschiedenen heavy/lightchain subcleasses

# Anzahl und Namen der verschiedenen heavy chain subclasses
unique_heavy_subclasses = df2['heavy_subclass'].dropna().unique()
print("Anzahl verschiedener Heavy-Subklassen:", len(unique_heavy_subclasses))
print("Heavy-Subklassen:", unique_heavy_subclasses)
# Anzahl und Namen der verschiedenen light chain subclasses
unique_light_subclasses = df2['light_subclass'].dropna().unique()
print("Anzahl verschiedener Light-Subklassen:", len(unique_light_subclasses))
print("Light-Subklassen:", unique_light_subclasses)
# Kombinationen aus heavy_subclass und light_subclass
kombinationen = df2[["heavy_subclass", "light_subclass"]].dropna()
# Einzigartige Kombinationen zählen
anzahl_kombinationen = kombinationen.drop_duplicates().shape[0]
print("Anzahl verschiedener Heavy-Light-Subklassen-Kombinationen:", anzahl_kombinationen)
# Optional: Auch alle Kombinationen anzeigen
print("\nKombinationen:")
print(kombinationen.drop_duplicates())





# welche Methode ist für uns am wichtigsten ? (unsere 3 Kategorien und den jeweiligen method count)

# Liste der relevanten Arten (exakte Begriffe, aber ohne Beachtung von Groß-/Kleinschreibung)
relevant_species = [
    "severe acute respiratory syndrome coronavirus2",
    "severe acute respiratory syndrome coronavirus",
    "homo sapiens"
]
# Spalte in Kleinbuchstaben umwandeln, um Vergleich zu erleichtern
df2['antigen_species_clean'] = df2['antigen_species'].str.strip().str.lower()
# Nur Zeilen behalten, in denen antigen_species exakt in der Liste enthalten ist
df_filtered = df2[df2['antigen_species_clean'].isin(relevant_species)].copy()
# Gruppieren nach 'antigen_species' (Originalspalte!) und 'method' und Anzahl zählen
method_counts = df_filtered.groupby(['antigen_species', 'method']).size().reset_index(name='count')
# Nach Art und Häufigkeit sortieren
method_counts = method_counts.sort_values(by=['antigen_species', 'count'], ascending=[True, False])
# Ausgabe
print(method_counts)




#coulumn antigen_species Filter nach unseren 3 Kategorien
# Gesuchte Begriffe
terms = [
    "severe acute respiratory syndrome coronavirus2",
    "severe acute respiratory syndrome coronavirus",
    "homo sapiens"
]

# Leere Dictionary für Ergebnisse
results = {}

# Für jeden Begriff: finde alle einzigartigen passenden Einträge (Groß-/Kleinschreibung ignorieren)
for term in terms:
    matching_entries = df2[df2['antigen_species'].str.contains(term, case=False, na=False)]['antigen_species'].unique()
    results[term] = matching_entries

# Ergebnisse anzeigen
for term, entries in results.items():
    print(f"\nEinträge mit '{term}':")
    for entry in entries:
        print("-", entry)