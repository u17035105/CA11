#1. Import functions
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
df = pd.read_csv("C:/Users/Louise19/Desktop/class activity 11 data/mpg.csv")

#Added Calculated column
df["Displacement_To_Weight"] = df["displacement"] / df["weight"]

print(df)

#Subset of data
eightcylinders = df[df.cylinders == 8]

print(eightcylinders)

# Correlation 
correlation = eightcylinders["displacement"].corr(eightcylinders["weight"])


print(correlation)

seventy = df[df.model_year == 70]
seventyone = df[df.model_year == 71]
seventytwo = df[df.model_year == 72]
seventythree = df[df.model_year == 73]
seventyfour = df[df.model_year == 74]
seventyfive = df[df.model_year == 75]
seventysix = df[df.model_year == 76]
seventyseven = df[df.model_year == 77]
seventyeight = df[df.model_year == 78]
seventynine = df[df.model_year == 79]
eighty = df[df.model_year == 80]
eightyone = df[df.model_year == 81]
eightytwo = df[df.model_year == 82]


plt.scatter(seventy.horsepower, seventy.model_year)
plt.scatter(seventyone.horsepower, seventyone.model_year)
plt.scatter(seventytwo.horsepower, seventytwo.model_year)
plt.scatter(seventythree.horsepower, seventythree.model_year)
plt.scatter(seventyfour.horsepower, seventyfour.model_year)
plt.scatter(seventyfive.horsepower, seventyfive.model_year)
plt.scatter(seventysix.horsepower, seventysix.model_year)
plt.scatter(seventyseven.horsepower, seventyseven.model_year)
plt.scatter(seventyeight.horsepower, seventyeight.model_year)
plt.scatter(seventynine.horsepower, seventynine.model_year)
plt.scatter(eighty.horsepower, eighty.model_year)
plt.scatter(eightyone.horsepower, eightyone.model_year)
plt.scatter(eightytwo.horsepower, eightytwo.model_year)
plt.legend(['1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982' ])
plt.xlabel('Horsepower')
plt.ylabel('Model year')
plt.title('How the YearModel impacts the horsepower of a vehicle')
plt.show()
