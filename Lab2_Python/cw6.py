import numpy as np
from scipy.stats import describe, norm

# Parametry rozkładu normalnego
srednia = 0
odchylenie_standardowe = 2
liczba_danych = 100

def porownaj_statystyki(liczba_danych):
    dane = np.random.normal(loc=srednia, scale=odchylenie_standardowe, size=liczba_danych)
    statystyki_opisowe = describe(dane)


    print(f"Liczba danych: {liczba_danych}")
    print("Statystyki opisowe dla danych:")
    print(statystyki_opisowe)
    print("\nWartości teoretyczne:")
    print(f"Teoretyczna średnia: {srednia}")
    print(f"Teoretyczne odchylenie standardowe: {odchylenie_standardowe}\n")

porownaj_statystyki(100)
porownaj_statystyki(1000)
porownaj_statystyki(10000)
