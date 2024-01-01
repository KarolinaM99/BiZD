import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


srednia_hist = 1
odchylenie_standardowe_hist = 2

srednia_standard = 0
odchylenie_standardowe_standard = 1

srednia_gestosc = -1
odchylenie_standardowe_gestosc = 0.5

dane_hist = np.random.normal(loc=srednia_hist, scale=odchylenie_standardowe_hist, size=1000)

dane_standard = np.random.normal(loc=srednia_standard, scale=odchylenie_standardowe_standard, size=1000)

x_values_gestosc = np.linspace(-5, 3, 1000)
y_values_gestosc = norm.pdf(x_values_gestosc, loc=srednia_gestosc, scale=odchylenie_standardowe_gestosc)

plt.hist(dane_hist, bins=30, density=True, alpha=0.7, color='blue', label='Histogram')

plt.plot(x_values_gestosc, norm.pdf(x_values_gestosc, loc=srednia_standard, scale=odchylenie_standardowe_standard),
         'k-', linewidth=2, label='Rozkład standardowy')

plt.plot(x_values_gestosc, y_values_gestosc, 'r-', linewidth=2, label='Wykres gęstości')

plt.legend()
plt.title('Histogram, rozkład standardowy i wykres gęstości')
plt.xlabel('Wartość')
plt.ylabel('Gęstość')

plt.show()
