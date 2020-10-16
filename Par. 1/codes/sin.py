import math, numpy

pi = 3.1415926535897932384626433832795028841971693993751058209749445923

x = float(input('valor de x: ')) * (pi / 180)
n =50

def sinX(x,n):
    S = 0
    for i in range(n):
        signo = (-1)**i
        a = x**((2*i)+1)
        S =S + signo*a / math.factorial((2*i)+1)
    return S

S = sinX(x,n)

print('Valor real: ', math.sin(x))
print('Itearciones :', n)
error  = math.sin(x) - S
print('Aprocimación: ', S, 'con un error de ', numpy.format_float_scientific(error, exp_digits = 10))
#(s, exp_digits=4)