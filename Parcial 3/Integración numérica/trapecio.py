import math
from numpy import *
#f = lambda s: (4)/(1+s**2)
def trapecio(a,b,n, real, f):
    h = (b-a)/n
    r = f(a)
    for i in range(1,n):
        r+=2* f(a+i*h)
    r += f(b)
    r = (h/2)*(r)
    error = abs(r-real)
    print("Trapecio resultado: ", r, ", error: ", error)

def trapecio2(v,h, d, factor):
    #v= [146,122,76,54,40,30,14]
    #h = 20
    r = v[0]
    for i in range(1,len(v)-1):
        r+=2*v[i]
    r += v[len(v)-1]
    r = (h/2)*(r)
    #error = abs(r-real)
    #print("Trapecio: resultado: ", r, ", error: ", error)
    print("Trapecio, Área:",r)
    
