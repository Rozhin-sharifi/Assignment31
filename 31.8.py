import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import graphviz

df=pandas.read_csv("Assignment31/shows.csv")
print(df)

d={'UK':0, 'USA':1, 'N':2}
df['Nationality']=df['Nationality'].map(d)
d={'YES':1, 'NO':0}
df['Go']=df['Go'].map(d)
print(df)

features=['Age','Experience','Rank','Nationality']
x=df[features]
y=df['Go']

print(x)
print(y)

dtree=DecisionTreeClassifier()
dtree=dtree.fit(x,y)
data=tree.export_graphviz(dtree,out_file=None,feature_names=features)
graph=pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot=plt.imshow(img)
plt.show()

print(dtree.predict([[40,10,7,1]]))