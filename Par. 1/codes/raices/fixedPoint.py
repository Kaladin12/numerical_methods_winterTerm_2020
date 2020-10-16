import math

g = lambda x: math.e**(math.log1p(1)/x)
#fp = lambda x : -3*(math.log1p(-1+x)/x**4) - 2*x*(math.log1p(9)/math.log1p(x-1)) + x*(math.log1p(9)/(math.log1p(x-1)**2)) + 1/x**4
X_0 = 2

def fixedPoint(x_i, n):
    for i in range(n):
        x = x_i
        x_i = g(x)
    return x

print(fixedPoint(X_0, 10))
