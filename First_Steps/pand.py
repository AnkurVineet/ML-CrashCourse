import pandas as pd
import matplotlib.pyplot as plt
print(pd.__version__)
city_names = pd.Series(['New Delhi','Mumbai','Vadodara'])
population = pd.Series([500000,400000,200000])
population = population * 10
cities = pd.DataFrame({'City name': city_names,'Population': population})
print(cities[0:2])
#print(cities[0:2])

'''
Local Implementation
california_housing_dataframe = pd.read_csv("file://localhost/C://Users/DELL/Documents/GitHub/ML-CrashCourse/First_Steps/california_housing_train.csv",sep=",")
'''
california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv",sep=",")
print(california_housing_dataframe.describe())
california_housing_dataframe.hist('housing_median_age')
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
cities['exer'] = cities['City name'].apply(lambda val: val.startswith('San')) & cities['Area square miles'].apply(lambda val: val > 50)
print(cities)
print(cities.reindex([6,2,0]))
plt.show()
