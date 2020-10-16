import math

f = lambda x,powr, a: x**powr - a
fDerivative = lambda x, powr: powr*x**(powr-1)

def root(x_i,powr,n,a):
    for i in range(n):
        x = x_i - (f(x_i,powr,a)/fDerivative(x_i,powr))
        x_i = x
    return x

x = lambda a:math.sin(a)


print(root(5, 3,10,64))
