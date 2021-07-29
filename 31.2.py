import numpy
import matplotlib.pyplot as plt

speed=[99,86,87,88,111,86,103,87,94,78,77,85,86]
x=numpy.random.uniform(0,5,250)
plt.hist(x,5)
plt.show()
y=numpy.random.normal(5,1,10000)
plt.hist(y,100)
plt.show()
w=numpy.random.normal(5,1,1000)
z=numpy.random.normal(10,2,1000)

plt.scatter(w,z)
plt.show()