import statistics
import numpy as np

data = np.loadtxt("Wzrost.csv",delimiter=",")
mean_value = statistics.mean(data)
variance_value = statistics.variance(data)
std_deviation_value = statistics.stdev(data)


print(f"Średnia wartość: {mean_value}")
print(f"Wariancja: {variance_value}")
print(f"Odchylenie standardowe: {std_deviation_value}")
