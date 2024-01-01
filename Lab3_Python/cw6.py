import pandas as pd
from scipy.stats import ttest_ind


df = pd.read_csv('napoje.csv', delimiter=";")

regionalne_2001 = df.loc[df['rok'] == 2001, 'regionalne']
regionalne_2015 = df.loc[df['rok'] == 2015, 'regionalne']

stat, p_value = ttest_ind(regionalne_2001, regionalne_2015, equal_var=False)

print("Statystyka t:", stat)
print("Wartość p:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Odrzucamy hipotezę zerową - istnieją istotne różnice między średnimi.")
else:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej - brak istotnych różnic między średnimi.")
