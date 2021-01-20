import math
from numpy import *
from sympy import *
def simpson2(n, a,b, real, f):#4/(1+v**2)#math.sin(v)#4*math.sqrt(1-v**2)
    nPoints = n+1
    h = (b-a)/n
    s = f(a)
    for i in range(1,n):
        if (i%3==0):
            #print("3",i)
            s += 2*f(a+i*h)
        else:
            #print("2",i)
            s += 3*f(a+i*h)
    s += f(b)
    result = (3*h/8)*s
    error = abs(result-real)
    print("Tres octavos, resultado: ", result, ", error: ", error)

n=3
print("Función:  1/((x^2+1)(x-2)) [0,1]")
print("n:", n)
simpson2(n,0,1,-1*0.522103419527, lambda v: 1/((v**2+1)*(v-2)))