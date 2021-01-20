import math

f = lambda x: math.sin(x)/(x**2+1)
fp = lambda x : (math.cos(x)+x**2*math.cos(x) - 2*x*math.sin(x))/(1+x**2)**2

def newton(x_not, n):
    for i in range(n):
        x = x_not - (f(x_not)/fp(x_not))
        x_not = x
    return x

print("Raíz 1",newton(0.5, 10))
