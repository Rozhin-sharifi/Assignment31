import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale=StandardScaler()

df=pandas.read_csv("Assignment31/cars.csv")
x=df[['Weight','Volume']]
y=df['CO2']

scaledx=scale.fit_transform(x)
print(scaledx)
regr=linear_model.LinearRegression()
regr.fit(scaledx,y)
scaled=scale.transform([[2300,1.3]])
predictedCO2=regr.predict(scaled)
print(predictedCO2)
print(scaled)