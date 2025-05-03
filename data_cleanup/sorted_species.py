import pandas as pd
table = pd.read_csv("data/ab_ag.tsv", sep = "\t")
table_sorted = table["antigen_species"].unique()
print(table_sorted)
