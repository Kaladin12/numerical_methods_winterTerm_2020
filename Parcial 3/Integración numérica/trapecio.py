import math
from numpy import *
#f = lambda s: (4)/(1+s**2)
f = lambda s:s**2
def trapecio(a,b,n):
    real = 2
    h = (b-a)/n
    r = f(a)
    for i in range(1,n):
        r+=2* f(a+i*h)
    r += f(b)
    r = (h/2)*(r)
    error = abs(r-real)
    print("resultado: ", r, ", error: ", error)
trapecio(0,4, 40)