#Hecho por Elian Javier Cruz Esquivel

import math

realRootTan = 4.49340945790906
realRootXtoX = 1.55961

def newtonTanget(x_i, n):
    print("Método de Newton para x-tan(x)" )
    tan = lambda x: x - math.tan(x)
    tanDerivative = lambda x : 1-(1/math.cos(x))**2
    for i in range(n):
        x = x_i - (tan(x_i)/tanDerivative(x_i))
        print("x: "+str(x), "x_i"+str(x_i), "{:3e}".format(abs(realRootTan-x)))
        x_i = x
    return x

def newtonXtoTheX(x_i, n):
    print("\nMétodo de Newton para x^x - 2" )
    f = lambda x: x**x - 2
    fDerivative = lambda x: (x**x)*(math.log1p(x-1)+1)
    for i in range(n):
        x = x_i - (f(x_i)/fDerivative(x_i))
        print("x: "+str(x),"x_i: "+ str(x_i),"error: "+ "{:3e}".format(abs(realRootXtoX-x)))
        x_i = x
    return x

rTan = newtonTanget(4.3,15)
print("Número de iteraciones: ", 15)
print("la raíz es ",rTan, "con un error de " ,"{:3e}".format(abs(rTan-realRootTan)))

rXtoX = newtonXtoTheX(1.5,15)
print("Número de iteraciones: ", 15)
print("la raíz es ",rXtoX, "con un error de " ,"{:3e}".format(abs(rXtoX-realRootXtoX)))