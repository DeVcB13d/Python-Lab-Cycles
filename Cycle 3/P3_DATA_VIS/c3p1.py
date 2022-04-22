import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("iris.csv")
data.frame['species']
print(Uni_species)
bargraph = data.plot.bar(x = 'Species', y = 'Id', fontsize='9')
plt.show()