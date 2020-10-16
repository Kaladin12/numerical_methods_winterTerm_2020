#Hecho por Elian Javier Cruz Esquivel


import math

pi = 3.1415926535897932384626433832795028841971693993751058209749445923

def piValue():
    print('Cálculo de '+'\u03C0')
    X=0
    i=0
    while abs(4*X-pi)>0.001:
        X += (((-1)**i)*(1)**(2*i+1))/(2*i+1)
        #print("Suma parcial: "+str(X), "Error: ","{:2e}".format(abs(pi - 4*X)))
        i+=1
    print('Valor real: ', pi)
    print('Iteraciones :', i)
    print('Aprocimación: ', 4*X, 'con un error de ', "{:2e}".format(abs(pi - 4*X)))

def eToX(x):
    print('Cálculo de e')
    S = 0
    k=0
    while abs(math.e - S)>0.001:
        S += ((x)**k)/(math.factorial(k))
        #print("Suma parcial: "+str(S), "Error: ", "{:2e}".format(abs(math.e - S)))
        k+=1
    print('Valor real: ', math.e)
    print('Iteraciones :', k)
    print('Aprocimación: ', S, 'con un error de ', "{:2e}".format(abs(math.e - S)))

def etOXSquared(x):
    print('Cálculo de e^2')
    S = 0
    k = 0
    while abs((math.e)**2 - S)>0.001:
        S += ((2*x)**(k))/(math.factorial(k))
        #print("Suma parcial: "+str(S), "Error: ", "{:2e}".format(abs(math.e**2 - S)))
        k+=1
    print('Valor real: ', (math.e)**2)
    print('Iteraciones :', k)
    print('Aprocimación: ', S, 'con un error de ', "{:2e}".format(abs((math.e)**2 - S)))    

def naturalLogXPlusOne(x):
    print('Cálculo de ln(2)')
    S = 0.0
    i = 0
    while abs(S-math.log1p(1))>0.001:
        S += (-1)**(i) * (x**(i+1)) / (i+1)
        #print("Suma parcial: "+str(S), "Error: ", "{:2e}".format(abs(math.log1p(1) - S)))
        i+=1
    print('Valor real: ', math.log1p(1))
    print('Iteraciones :', i)
    print('Aprocimación: ', S, 'con un error de ', "{:2e}".format(abs(math.log1p(1) - S)))

piValue()
print('\n')
eToX(1)
print('\n')
etOXSquared(1)
print('\n')
naturalLogXPlusOne(1)
print('\n')