from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import binom

n_dwumianowy = 20
p_dwumianowy = 0.4

k_values = np.arange(0, n_dwumianowy + 1)
pmf_dwumianowy = binom.pmf(k_values, n_dwumianowy, p_dwumianowy)
suma_prawdopodobienstw = np.sum(pmf_dwumianowy)

plt.bar(k_values, pmf_dwumianowy, align='center', alpha=0.7)
plt.title('Rozkład Dwumianowy')
plt.xlabel('Liczba sukcesów (k)')
plt.ylabel('Prawdopodobieństwo')
plt.show()

print(f'Suma prawdopodobieństw: {suma_prawdopodobienstw:.2f}')
