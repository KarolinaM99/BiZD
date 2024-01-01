import numpy as np


wartosci = np.array([1, 2, 3, 4, 5, 6])
prawdopodobienstwa = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

oczekiwana_wartosc = np.sum(wartosci * prawdopodobienstwa)
wariancja = np.sum(prawdopodobienstwa * (wartosci - oczekiwana_wartosc)**2)
odchylenie_standardowe = np.sqrt(wariancja)
minimalne_wartosci = np.min(wartosci)
maksymalne_wartosci = np.max(wartosci)

print("Oczekiwana wartość:", oczekiwana_wartosc)
print("Wariancja:", wariancja)
print("Odchylenie standardowe:", odchylenie_standardowe)
print("Minimalne wartości:", minimalne_wartosci)
print("Maksymalne wartości:", maksymalne_wartosci)
