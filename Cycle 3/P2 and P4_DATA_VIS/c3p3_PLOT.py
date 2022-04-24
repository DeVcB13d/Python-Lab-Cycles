
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

'''PLOTTING THE BAR GRAPH'''
#Reading the CSV file using pandas
data = pd.read_csv("iris.csv")
#Plotting bar graph with frequencies
Species_list = data['Species'].value_counts()
Species_list.plot(kind = "bar",xlabel = 'frequency',ylabel= 'species')
plt.show()

'''PLOTTING SCATTER PLOT'''

'''Preprocessing of the data'''
#Appling PCA to get 2 principal compnents
from sklearn.preprocessing import StandardScaler
#Removing species column
x  = data.iloc[:,:-1]
print(x)
x = StandardScaler().fit_transform(x) #normalising the data
#After normalisation mean = 0 and std dvn = 1
print("Mean",np.mean(x))
print("STD Dvn : ",np.std(x))

#Calculating PCA to get 2 components
from sklearn.decomposition import PCA
pca_iris =  PCA(n_components=2)
print(pca_iris)
principal_components_iris = pca_iris.fit_transform(x)
print(principal_components_iris)
#Creating a data frame with PCA Values
principal_iris_DF = pd.DataFrame(data=principal_components_iris,
        columns = ['PC1','PC2'])
principal_iris_DF.tail()
print(principal_iris_DF)
'''Plotting from the principal Components'''
plt.figure()
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
targets = ['Iris-setosa','Iris-versicolor','Iris-virginica']
colors = ['r','g','b']
for target,color in  zip(targets,colors):
    indices_to_Keep = data['Species'] == target
    plt.scatter(principal_iris_DF.loc[indices_to_Keep,'PC1'],
    principal_iris_DF.loc[indices_to_Keep,"PC2"],c = color)
plt.show()
'''PLOTTING OF EACH ATTRIBUTE AS A HISTOGRAM'''
#To show each attribute as a histogram
def plot_hist(Att_name,Hcolor,title,xtitle):
    data[Att_name].hist(color = Hcolor)
    plt.xlabel(xtitle)
    plt.ylabel('frequency')
    plt.title(title)
    plt.show()

plot_hist('SepalLengthCm','r','Sepal length distribution','sepal length(cm)')
plot_hist('SepalWidthCm','g','Sepal Width distribution','sepal width(cm)')
plot_hist('PetalLengthCm','b','Petal length distribution','petal length(cm)')
plot_hist('PetalWidthCm','grey','Petal width distribution','petal width(cm)')











































