import math

x = 1
n = 1000

def eToX(x,n):
    S = 0
    for k in range(n):
        S += ((x)**k)/(math.factorial(k))
    return S
    
S = eToX(x,n)

print('Valor real: ', math.e)
print('Itearciones :', n)
print('Aprocimación: ', S, 'con un error de ', math.e - S)