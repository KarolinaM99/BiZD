import numpy as np
from scipy.stats import ttest_1samp


srednia = 2
odchylenie = 30
liczba_elementow = 200

probka = np.random.normal(srednia, odchylenie, liczba_elementow)

hipoteza_srednia = 2.5

statystyka_t, p_value = ttest_1samp(probka, hipoteza_srednia)

print("Statystyka t:", statystyka_t)
print("Wartość p:", p_value)

alfa = 0.05  
if p_value < alfa:
    print("Odrzucamy hipotezę zerową - istnieją istotne różnice.")
else:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej.")
