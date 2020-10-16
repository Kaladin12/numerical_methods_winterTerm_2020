import math

S = 0
x = int(input("valor de x: "))
n = int(input("iteraciones: "))

for i in range(n):
    S += (-1)**(i) * (x**(i+1)) / (i+1)

print('Valor real: ', math.log1p(1))
print('Itearciones :', n)
print('Aprocimación: ', S, 'con un error de ', math.log1p(1) - S)