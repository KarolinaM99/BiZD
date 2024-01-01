import pandas as pd
from scipy.stats import levene

df = pd.read_csv('napoje.csv', delimiter=";")

pary_war = [('okocim', 'lech'), ('żywiec', 'fanta '), ('regionalne', 'cola')]

for para in pary_war:
    zmienna1, zmienna2 = para
    stat, p_value = levene(df[zmienna1], df[zmienna2])
    
    print(f"Pary: {zmienna1} - {zmienna2}")
    print(f"Statystyka testu: {stat}")
    print(f"Wartość p: {p_value}")
    
    alpha = 0.05
    if p_value < alpha:
        print("Odrzucamy hipotezę zerową - istnieją istotne różnice w wariancjach.")
    else:
        print("Nie ma podstaw do odrzucenia hipotezy zerowej - brak istotnych różnic w wariancjach.")
    
    print("__________________")
