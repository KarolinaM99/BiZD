import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv('napoje.csv', delimiter=";")

pary = [('okocim', 'lech'), ('fanta ', 'regionalne'), ('cola', 'pepsi')]

for para in pary:
    zmienna1, zmienna2 = para
    stat, p_value = ttest_ind(df[zmienna1], df[zmienna2], equal_var=False)
    
    print(f"Pary: {zmienna1} - {zmienna2}")
    print(f"Statystyka t: {stat}")
    print(f"Wartość p: {p_value}")
    
    alpha = 0.05
    if p_value < alpha:
        print("Odrzucamy hipotezę zerową - istnieją istotne różnice między średnimi.")
    else:
        print("Nie ma podstaw do odrzucenia hipotezy zerowej - brak istotnych różnic między średnimi.")
    
    print("_____________")
