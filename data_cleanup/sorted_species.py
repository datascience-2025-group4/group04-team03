import pandas as pd
table_antigen_species = pd.read_csv("data/ab_ag.tsv", sep = "\t")
table_sorted = table_antigen_species["antigen_species"].unique()
print(table_sorted)

name_counts = table_antigen_species["antigen_species"].value_counts().sort_index()
print(name_counts)
name_counts_df = name_counts.reset_index()
name_counts_df.columns = ['antigen_species', 'count']
print(name_counts_df)
