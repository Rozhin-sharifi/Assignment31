import numpy
from scipy import stats

speed=[99,86,87,88,111,86,103,87,94,78,77,85,86]

x=numpy.mean(speed)
y=numpy.median(speed)
z=stats.mode(speed)[0]
w=numpy.std(speed)
f=numpy.var(speed)
g=numpy.percentile(speed,75)
print(x,y,z,w,f,g)


