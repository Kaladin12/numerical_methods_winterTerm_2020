import math

realroot = math.pi
X = 2

def tanx(x_i, n):
    tan = lambda x: math.tan(x)
    tanDerivative = lambda x: (1/math.cos(x))**2
    for i in range(n):
        x = x_i - (tan(x_i)/tanDerivative(x_i))
        print(x_i, x)
        x_i = x
    return x

print(tanx(X, 20))