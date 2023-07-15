import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from scipy.stats import pearsonr

# Calcola il Mean Absolute Error / computes Mean Absolute Error (MAE)
def mae(arr_effettivi, arr_predetti):
    return np.mean(np.abs(arr_effettivi - arr_predetti))

# Calcola Pearson's r / computes Pearson's r
def pearson(arr_effettivi, arr_predetti):
    return(pearsonr(arr_effettivi, arr_predetti))

# Legge i file con le annotazioni originali ('effettivi.csv') e i file ricevuti dai partecipanti ('predetti.csv')
# Read the files with original annotations ('effettivi.csv') and the ones received from partecipants ('predetti.csv')
df_effettivi=pd.read_csv('effettivi.csv')
df_predetti=pd.read_csv('predetti.csv')

#Converte il dataframe pandas in array numpy, colonna per colonna /converts pandas dataframe to numpy's array.

arr_effettivi_V=df_effettivi.VE.to_numpy()
arr_predetti_V=df_predetti.V.to_numpy()
arr_effettivi_A=df_effettivi.AE.to_numpy()
arr_predetti_A=df_predetti.A.to_numpy()
arr_effettivi_D=df_effettivi.DE.to_numpy()
arr_predetti_D=df_predetti.D.to_numpy()

# Ottiene i valori di Pearson's r e MAE / Gets the values for Pearson's r and MAE
r_V= pearson(arr_effettivi_V, arr_predetti_V)
r_A= pearson(arr_effettivi_A, arr_predetti_A)
r_D= pearson(arr_effettivi_D, arr_predetti_D)

MAE_V= mae(arr_effettivi_V, arr_predetti_V)
MAE_A= mae(arr_effettivi_A, arr_predetti_A)
MAE_D= mae(arr_effettivi_D, arr_predetti_D)

#Stampiamo i risultati / print results on screen
print("r V: ", r_V, '\n', "r A: ", r_A, '\n', "r D: ", r_D, '\n', "MAE V: ", MAE_V, '\n', "MAE A: ", MAE_A, '\n', "MAE D: ", MAE_D, '\n')

#Salviamo i risultati / Saves results to file
with open('risultati.txt', 'a') as ris_file:
        ris_file.write("Pearson's r V: " + str(r_V))
        ris_file.write("\n")
        ris_file.write("Pearson's r A: " + str(r_A))
        ris_file.write("\n")
        ris_file.write("Pearson's r D: " + str(r_D))
        ris_file.write("\n")
        ris_file.write("MAE V: " + str(MAE_V))
        ris_file.write("\n")
        ris_file.write("MAE A: " + str(MAE_A))
        ris_file.write("\n")
        ris_file.write("MAE D: " + str(MAE_D))
        ris_file.write("\n")