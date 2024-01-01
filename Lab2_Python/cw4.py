import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

#Rozkład Bernoulliego
p_bernoulli = 0.3
x_values_bernoulli = np.array([0, 1])
y_values_bernoulli = [1 - p_bernoulli, p_bernoulli]

#Rozkładu Dwumianowy
n_binomial = 10
p_binomial = 0.5
x_values_binomial = np.arange(0, n_binomial + 1)
y_values_binomial = binom.pmf(x_values_binomial, n_binomial, p_binomial)

#Rozkład Poissona
lambda_poisson = 3.0
x_values_poisson = np.arange(0, 15)
y_values_poisson = poisson.pmf(x_values_poisson, lambda_poisson)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.bar(x_values_bernoulli, y_values_bernoulli, align='center', alpha=0.7)
plt.title('Rozkład Bernoulliego')
plt.xlabel('Wartość')
plt.ylabel('Prawdopodobieństwo')

plt.subplot(1, 3, 2)
plt.bar(x_values_binomial, y_values_binomial, align='center', alpha=0.7)
plt.title('Rozkład Dwumianowy')
plt.xlabel('Liczba sukcesów')
plt.ylabel('Prawdopodobieństwo')

plt.subplot(1, 3, 3)
plt.bar(x_values_poisson, y_values_poisson, align='center', alpha=0.7)
plt.title('Rozkład Poissona')
plt.xlabel('Liczba zdarzeń')
plt.ylabel('Prawdopodobieństwo')

plt.tight_layout()
plt.show()
