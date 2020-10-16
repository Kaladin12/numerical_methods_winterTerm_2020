import math

x = 1
n = 1000
S = 0
for k in range(n):
    S += ((2*x)**(k))/(math.factorial(k))

print('Valor real: ', (math.e)**2)
print('Itearciones :', n)
print('Aprocimación: ', S, 'con un error de ', (math.e)**2 - S)