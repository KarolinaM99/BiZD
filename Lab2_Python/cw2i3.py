import numpy as np
from scipy.stats import describe, kurtosis, skew

#Rozkład Bernoulliego
p = 0.3
proba_bernoulliego = np.random.choice([0, 1], size=100, p=[1-p, p])

print("Próba rozkładu Bernoulliego:")
print(proba_bernoulliego)

stats_bernoulli = describe(proba_bernoulliego)
kurtoza_bernoulli = kurtosis(proba_bernoulliego)
skosnosc_bernoulli = skew(proba_bernoulliego)

print("Statystyki dla rozkładu Bernoulliego:")
print(f"Średnia: {stats_bernoulli.mean}")
print(f"Wariancja: {stats_bernoulli.variance}")
print(f"Kurtoza: {kurtoza_bernoulli}")
print(f"Skośność: {skosnosc_bernoulli}\n")

#Rozkład Dwumianowy 
n_dwumianowy = 10
p_dwumianowy = 0.5
proba_dwumianowego = np.random.binomial(n=n_dwumianowy, p=p_dwumianowy, size=100)

print("Próba rozkładu Dwumianowego:")
print(proba_dwumianowego)

stats_binomial = describe(proba_dwumianowego)
kurtoza_binomial = kurtosis(proba_dwumianowego)
skosnosc_binomial = skew(proba_dwumianowego)

print("Statystyki dla rozkładu Dwumianowego:")
print(f"Średnia: {stats_binomial.mean}")
print(f"Wariancja: {stats_binomial.variance}")
print(f"Kurtoza: {kurtoza_binomial}")
print(f"Skośność: {skosnosc_binomial}\n")

#Rozkład Poissona
lambda_poissona = 3.0
proba_poissona = np.random.poisson(lam=lambda_poissona, size=100)

print("Próba rozkładu Poissona:")
print(proba_poissona)

stats_poisson = describe(proba_poissona)
kurtoza_poisson = kurtosis(proba_poissona)
skosnosc_poisson = skew(proba_poissona)

print("Statystyki dla rozkładu Poissona:")
print(f"Średnia: {stats_poisson.mean}")
print(f"Wariancja: {stats_poisson.variance}")
print(f"Kurtoza: {kurtoza_poisson}")
print(f"Skośność: {skosnosc_poisson}")