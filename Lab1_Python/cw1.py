import pandas as pd
import numpy as np

data = pd.read_csv("MDR_RR_TB_burden_estimates_2023-12-05.csv", usecols=["e_rr_pct_new"])
print("Maksymalny wzrost:", data.max())
print("Maksymalny wzrost, funkcja:", np.max(data))
print("Minimalny wzrost:", data.min())
print("Minimalny wzrost, funkcja:", np.min(data))
print("Średni wzrost:", data.mean())
print("Średni wzrost, funkcja:", np.mean(data))
print("Odchylenie standardowe, wzrost:", data.std())
print("Odchylenie standardowe, wzrost, funkcja:", np.std(data))
print("Mediana:", np.median(data))
print("Wartość na 50 procencie:", np.percentile(data, 50))
