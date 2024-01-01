import pandas as pd
from scipy.stats import shapiro


df = pd.read_csv('napoje.csv', delimiter=";")

zmienne = df.columns

for zmienna in zmienne:
    stat, p_value = shapiro(df[zmienna])
    
    print(f"Zmienna: {zmienna}")
    print(f"Statystyka testu: {stat}")
    print(f"Wartość p: {p_value}")
    
    alpha = 0.05
    if p_value > alpha:
        print("Rozkład jest normalny (nie ma podstaw do odrzucenia hipotezy zerowej).")
    else:
        print("Rozkład nie jest normalny (odrzucamy hipotezę zerową o normalności).")
    
    print("____________________")
