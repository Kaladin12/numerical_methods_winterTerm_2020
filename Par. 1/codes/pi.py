import math

pi = 3.1415926535897932384626433832795028841971693993751058209749445923

n=100000
X=0
for i in range(n):
    X += (((-1)**i)*(1)**(2*i+1))/(2*i+1)

print('Valor real: ', pi)
print('Itearciones :', n)
print('Aprocimación: ', 4*X, 'con un error de ', pi - 4*X)
