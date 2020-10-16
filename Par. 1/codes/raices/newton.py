import math

f = lambda x: math.cos(x*math.pi)
fp = lambda x : -3*(math.log1p(-1+x)/x**4) - 2*x*(math.log1p(9)/math.log1p(x-1)) + x*(math.log1p(9)/(math.log1p(x-1)**2)) + 1/x**4
X = 1.3

def newton(x_not, n):
    for i in range(n):
        x = x_not - (f(x_not)/fp(x_not))
        print(x_not, x)
        x_not = x
    return x

print(newton(X, 15))
