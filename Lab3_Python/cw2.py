import pandas as pd
from scipy.stats import ttest_1samp


df = pd.read_csv('napoje.csv',delimiter=";")

lech_mean = 60500
lech_column = 'lech'

statistic_lech, p_value_lech = ttest_1samp(df[lech_column], lech_mean)

print(f"Statystyka t dla spożycia piwa Lech: {statistic_lech}")
print(f"Wartość p dla spożycia piwa Lech: {p_value_lech}")

cola_mean = 222000
cola_column = 'cola'

statistic_cola, p_value_cola = ttest_1samp(df[cola_column], cola_mean)

print(f"Statystyka t dla spożycia coli: {statistic_cola}")
print(f"Wartość p dla spożycia coli: {p_value_cola}")

regionalne_mean = 43500
regionalne_column = 'regionalne'

statistic_regionalne, p_value_regionalne = ttest_1samp(df[regionalne_column], regionalne_mean)

print(f"Statystyka t dla spożycia piw regionalnych: {statistic_regionalne}")
print(f"Wartość p dla spożycia piw regionalnych: {p_value_regionalne}")
