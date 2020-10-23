import math

f = lambda x: math.e**x - math.sin(x)-x-2
fp = lambda x : math.e**x -math.cos(x)-1
X_2 = 2
X_1 = -1
def newton(x_not, n):
    for i in range(n):
        x = x_not - (f(x_not)/fp(x_not))
        x_not = x
    return x

print("Raíz 1",newton(X_1, 15))
print("Raíz 2",newton(X_2, 15))
