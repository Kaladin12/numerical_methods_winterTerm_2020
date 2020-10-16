import math

S = 0
x = float(input('valor de x: ')) * (math.pi / 180)
n =50

for i in range(n):
    signo = (-1)**i
    a = x**(2*i)
    S += signo*a / math.factorial(2*i)

print('Valor real: ', math.cos(x))
print('Itearciones :', n)
print('Aprocimación: ', S, 'con un error de ', math.cos(x)- S)