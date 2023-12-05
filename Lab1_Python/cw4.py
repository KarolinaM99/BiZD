import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("brain_size.csv",delimiter=";")

mean_viq = data['VIQ'].mean()
print(f"Średnia VIQ: {mean_viq}")

gender_counts = data['Gender'].value_counts()
print(f"Liczba kobiet: {gender_counts['Female']}")
print(f"Liczba mężczyzn: {gender_counts['Male']}")

data[['VIQ', 'PIQ', 'FSIQ']].hist()
plt.suptitle('Histogramy dla VIQ, PIQ, FSIQ')
plt.show()

data[data['Gender'] == 'Female'][['VIQ', 'PIQ', 'FSIQ']].hist()
plt.suptitle('Histogramy dla VIQ, PIQ, FSIQ (kobiety)')
plt.show()
