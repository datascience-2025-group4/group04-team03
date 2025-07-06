# How Antibody Gene Families and Sequences Influence Antigen Targeting

# group04-team03:
# Topic 04, Team 03: 

Contributors
----------
Tom Straube, Jurek Wunderlich, Annika Stöhr, Sandra Barth 


Supervisor
----------
_Prof. Dominik Niopek_  ([dominik.niopek@uni-heidelberg.de]) 
_Benedict Wolf_([benedict.wolf@uni-heidelberg.de])
_Jan Mathony_  ([jan.mathony@uni-heidelberg.de])

Tutor: _Enno Schäfer_ ([enno.schaefer@stud.uni-heidelberg.de])    


Research Question
----------
Our group´s goal was to explore the connection between antibody gene families and the antigen species they target. 
To do so, we mainly focused on analysing the aminoacid sequence of respective structures, assigning variable domains and CDR regions. 
With this approach we hoped to assing clusters to gene families, which target the same antigen species.
Furthermore heavy and light chains were observed separately, clustering them based on the consensus sequences - the calculated sequence based on the most frequent amino acid residues in each sequence within the gene family. 


Repository Structure
-----------------------------
First of all: We decided to include all files and data necessary to run the codespaces leading to our results in the repository. 
This way no external data apart form the nesessary packages needs to be downloaded in order to run the code.

Our repository consists of 5 folders:

- data 
- data_cleanup
- documentation
- blasting 
- archieve

All important results and plots can be found in the folder **blasting**
Storing our diffrent approaches, we created three sub-folders, in **blasting** to keep it structered. 

- **consensus_sequences**: 
  In this folder all results are stored based on heavy/light chain consensus sequences, further processed with multiple sequence alignment and clustering approaches to assign antigen species to specific antibody gene families. 
  It contains the aa seq. analysis of light chains and heavy chains, in diffrent documents: 

 - *heavy chains*: 
    all code for plots shown on the poster can be found in **heavy_results**
    the rest is stored in:**genfam_sequences.ipynb**, **consensus_genfam.ipynb** and **antigens_h_chains.ipynb**
 
 - *light chains*: 
    all code for plots shown on the poster can be found in **light_results**
    the rest is stored in:**blasting/mmseqs/light_chains.ipynb**, **blasting/mmseqs/light_chains_analysis.ipynb** and**consensus_genfam_lightchains.ipynb** 
 






- **domain_analysis**: 
This file contains the "Domain-Based Gene Family Analysis with InterProScan" which aims to detect short conserved amino acid motifs in domains of the light chain of immunoglobulins. And evaluates their association with gene family classification and antigen specificty.

To create the charts used in the poster presentation only the files lchains_1_ipr.tsv and master_df_1_light_antigen_category.csv are nesessary, these and the charts are uploaded into our teams github repository.

To learn about the insights our results provide open the jupyter notebook domain_analysis in the blasting folder.


TODO
- Force push pictures

- **Multiple Sequence Alignment**: 
This folder includes all results based on Multiple Sequence Alignment. The goal of this section was to examine a potential correlation between the antigen species targeted by an antibody and the amino acid sequence of the antibody.

The files to generate the plots used on the poster have already been pushed, to generate the plots, simply run the code in the file Visualization.ipynb. The input FASTA files for Multiple Sequence Alignment have also been pushed. To reproduce the analysis, sequentially run:

 Clustal_Omega.ipynb - performs Multiple Sequence Alignment
 distance_matrix.ipynb - generates distance matrix based on MSA
 PCA_Clustering.ipynb - reduces dimensions of the distance matrix with PCA and then clusters the data using kmeans clustering
 antigen_sequence_correlation.ipynb - Analyzes the correlation between the MSA based clustering and the targeted antigen species








Covering the mandatory aspects of the project
------------
Our project was supposed to contain the following elements. Here, we list which sub-topic covers which mandatory aspect: 
- **descriptive statistics** about the datasets: Domain Analysis (2.4, 2.5)
- **graphical representations**: all sub-topics
- **dimension reduction** analysis (PCA, clustering or k-means): all sub-topics
- **statistical tests** (t-test, proportion tests etc): all sub topics
- We did not implement a **linear regression**, which we discussed with our tutor Enno Schäfer beforehand.


Additional files and folders
---------
files for result code running 





Download the datasets worked on
----------
links for this folder 