# %% 
import pandas as pd
import re
#read file as a dataset, separating columns by tabs
df = pd.read_csv("data/uniprot_data.tsv", sep = "\t")

#first I want to clean the column "Protein names" and want to only leave the short names of the proteins (w/o the brackets),but i want to have access to both full and short version of the table

#the coloumn needs to be cleaned from bracket, exept the ones starting w G(), as they show the G-proteins
#new function "clean_brackets" is made for variable text
def clean_brackets(text):
    # square brackets are removed
    text = re.sub(r'\s*\[.*?\]', '', text)
    # round brackets are removed unless they start with 'G('
    text = re.sub(r'\s*(?<!G)\(.*?\)', '', text)
    return text.strip()

#applying the funtion
df_shortnames = df['Protein names'].apply(clean_brackets)

#replacing the column in df_short
df_short = df.copy()
df_short["Protein names"] = df_shortnames

# %%



# %%
#here I just sorted the column "Organism" so that it is in the alphabetical
df_sorted = df_short.sort_values(by= "Organism", ascending= True)
# %%

# %% 
#the same clean up of the brackets i execute in the column "Organism"
def clean_brackets(text):
    # square brackets are removed
    text = re.sub(r'\s*\[.*?\]', '', text)
    # round brackets are removed unless they start with 'G('
    text = re.sub(r'\s*(?<!G)\(.*?\)', '', text)
    return text.strip()

#applying the funtion
df_short_organism = df_sorted['Organism'].apply(clean_brackets)

#replacing the column in df_short
df_short = df_sorted.copy()
df_short["Organism"] = df_short_organism
# %%



#%%
#then reseting the indexes in the ascending order
df_short = df_short.reset_index(drop= True)
print(df_short)
# %%



# %% 
#the original dataset is stored as df_full and is also sorted by organisms, however the brackets are not deleted
df_full = df.sort_values(by= "Organism", ascending= True)
df_full = df_full.reset_index(drop= True)
print(df_full)
#%%
