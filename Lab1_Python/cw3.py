import pandas as pd
from scipy.stats import describe


data = pd.read_csv("MDR_RR_TB_burden_estimates_2023-12-05.csv",delimiter=",")
numeric_column = data["e_rr_pct_new"]
desc_stats = describe(numeric_column)


print("Statystyki opisowe:")
print(desc_stats)
