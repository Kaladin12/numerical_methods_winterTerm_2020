import math
from numpy import *
from sympy import *
real = 0
def simpson(n, a,b):
    f = lambda v: 2/(1-v**2)#math.sin(v)**2#4*math.sqrt(1-v**2)
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
    print(result)

simpson(30,0,0.99)