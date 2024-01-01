import pandas as pd
from scipy.stats import ttest_rel

df_2016 = pd.read_csv('napoje.csv', delimiter=";")
df_po_reklamie = pd.read_csv('napoje_po_reklamie.csv', delimiter=";")

zmienne = ['cola', 'fanta ', 'pepsi']

for zmienna in zmienne:
    wartości_2016 = df_2016[zmienna]
    wartości_po_reklamie = df_po_reklamie[zmienna]
    
    if len(wartości_2016) != len(wartości_po_reklamie):
        print(f"Error: The lengths of arrays for variable {zmienna} are not equal.")
        continue
    
    stat, p_value = ttest_rel(wartości_2016, wartości_po_reklamie)
    
    print(f"Zmienna: {zmienna}")
    print(f"Statystyka t: {stat}")
    print(f"Wartość p: {p_value}")
    
    alpha = 0.05
    if p_value < alpha:
        print("Odrzucamy hipotezę zerową - istnieją istotne różnice między średnimi.")
    else:
        print("Nie ma podstaw do odrzucenia hipotezy zerowej - brak istotnych różnic między średnimi.")
    
    print("_______________")
