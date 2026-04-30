import numpy as np
import matplotlib.pyplot as plt

def func(xVal):
    return np.sin(xVal*xVal)

def gaussOriginal(N):
    xVal, weight=np.polynomial.legendre.leggauss(N)
    return xVal, weight

def gaussInLimit(xInit,xFinal,xVal,weight):
    return 0.5*(xFinal-xInit)*xVal+0.5*(xFinal+xInit), 0.5*(xFinal-xInit)*weight

nVals=np.array([1,2,3,4,5,6,7,8,9,10])
integVals=np.zeros(nVals.size)

for i in range(nVals.size):
    gaussN=gaussOriginal(nVals[i])
    gaussNadj=gaussInLimit(0.0,np.pi,gaussN[0],gaussN[1])
    integVals[i]+=np.sum(func(gaussNadj[0])*gaussNadj[1])

plt.plot(nVals,integVals)
plt.grid()
plt.xlabel("Valor de N")
plt.ylabel("Aproximación de la integral")

plt.show
