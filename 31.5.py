import pandas
from sklearn import linear_model
df=pandas.read_csv("Assignment31/cars.csv")
x=df[['Weight','Volume']]
y=df['CO2']

regr=linear_model.LinearRegression()
regr.fit(x,y)

predictedCO2=regr.predict([[2300,1300]])
print(predictedCO2)
print(regr.coef_)