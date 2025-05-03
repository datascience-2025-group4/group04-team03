import pandas as pd
table_antigen_species = pd.read_csv("data/ab_ag.tsv", sep = "\t")

name_counts = table_antigen_species["antigen_species"].value_counts().sort_index()
name_counts_df = name_counts.reset_index()
name_counts_df.columns = ['antigen_species', 'count']
pd.set_option('display.max_rows', None) 
pd.set_option('display.max_columns', None)  
pd.set_option('display.width', None)  
pd.set_option('display.max_colwidth', None)
print(name_counts_df)
