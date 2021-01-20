import math
from numpy import *
from sympy import *
def simpson(n, a,b, real, f):
    #f = lambda v:  v*math.log1p(v-1) #math.sin(v)#4*math.sqrt(1-v**2)
    nPoints = n+1
    h = (b-a)/n
    s = f(a)
    for i in range(1,n):
        if (i%2==0):
            s += 2*f(a+i*h)
        else:
            s += 4*f(a+i*h)
    s += f(b)
    result = (h/3)*s
    error = abs(result-real)
    print("Un Tercio, resultado: ", result, ", error: ", error)

def simpsonVect(v,h, depth, factor):
    #f = lambda v:  v*math.log1p(v-1) #math.sin(v)#4*math.sqrt(1-v**2)
    n = len(v)
    s = v[0]
    for i in range(1,n):
        if (i%2==0):
            s += 2*v[i]
        else:
            s += 4*v[i]
    s += v[len(v)-1]
    result = (h/3)*s
    #error = abs(result-real)
    #print("Un Tercio, resultado: ", result, ", error: ", error)
    print("Simpson 1/3, Área:",result)


#n=6
#print("Función:  9pi/2 * sqrt(4+x^2) [0,2]")
#print("n:", n)
#simpson(n,0,2,75.3982236862,lambda v: (9*math.pi/2)*math.sqrt(4+v**2))