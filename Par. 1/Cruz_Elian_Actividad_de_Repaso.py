import math

root1 = 0.22849140
root2 = 2.69682

def serie():
    print('Serie de MacLaurin para ln((1+x)/(1-x)), evaluada en 0.75 para obtener ln(7)')
    S = 0
    x = .75
    real = 1.94591014906
    i = 0 
    while abs(S-real)>=0.00001:
        S += 2*(x)**(2*i + 1) / (2*i +1)
        print("S:", S, "error: "+"{:3e}".format(abs(S-real)))
        i+=1
    print("iteraciones: ", i)
    print(S, 'con un error absoluto de: ', "{:3e}".format(abs(S-real)))
    print('\n')
serie()

def raiz(a,b, a2,b2):
    print('Calculo de raices para 11x-2e^x mediante método de bisección \nRaíz 1: ')
    x = lambda s : 11*s - 2*(math.e)**s
    aN = a
    bN = b
    i = 0
    while abs((aN+bN)/2 - root1)>=0.00001:
        m_n = (aN+bN)/2
        f = x(m_n)
        print("a_N: "+str(aN),"b_N: "+str(bN),"m_N: "+str(m_n), "error: "+"{:3e}".format(abs(root1-(aN+bN)/2 )))
        if x(aN)*f < 0:
            bN = m_n
        elif x(bN)*f < 0:
            aN = m_n
        elif f == 0:
            return m_n
        else:
            return None
        i+=1
    print("iteraciones: ", i)
    print((aN+bN)/2, 'con un error absoluto de: ', "{:3e}".format(abs((aN+bN)/2-root1)))
    print('\nRaíz 2:')
    i = 0
    aN = a2
    bN = b2
    while abs((aN+bN)/2 - root2)>=0.00001:
        m_n = (aN+bN)/2
        f = x(m_n)
        print("a_N: "+str(aN),"b_N: "+str(bN),"m_N: "+str(m_n), "error: "+"{:3e}".format(abs(root2-(aN+bN)/2 )))
        if x(aN)*f < 0:
            bN = m_n
        elif x(bN)*f < 0:
            aN = m_n
        elif f == 0:
            return m_n
        else:
            return None
        i+=1
    print("iteraciones: ", i)
    print((aN+bN)/2, 'con un error absoluto de: ', "{:3e}".format(abs((aN+bN)/2-root2)))
    print('\n')
raiz(0,1,2,3)

def newton(x_0, x_0_2):
    print('Calculo de raices para 11x-2e^x mediante método de Nexton \nRaíz 1:')
    f = lambda x: 11*x - 2*(math.e)**x
    fp = lambda x : 11 - 2*(math.e)**x
    i=0
    x=0
    while abs(x-root1)>=0.00001:
        x = x_0 - (f(x_0)/fp(x_0))
        print("x_0: ",x_0,"x: ", x)
        x_0 = x
        i+=1
    print("iteraciones: ", i)
    print(x, 'con un error absoluto de: ', "{:3e}".format(abs(x-root1)))
    print('\nRaíz 2:')
    x_0 = x_0_2
    i=0
    x=0
    while abs(x-root2)>=0.00001:
        x = x_0 - (f(x_0)/fp(x_0))
        print("x_0: ",x_0,"x: ", x)
        x_0 = x
        i+=1
    print("iteraciones: ", i)
    print(x, 'con un error absoluto de: ', "{:3e}".format(abs(x-root2)))

newton(0,2)

def fixedPoint(x_0, x_0_2):
    print('Calculo de raices para 11x-2e^x mediante método de Punto Fijo \nRaíz 1:')
    print("g(x) = 2e^x/11")
    g = lambda x: 2*(math.e)**x / 11
    i=0
    x=0
    while abs(x-root1)>=0.00001:
        x = x_0
        print("x_0: ",x_0,"x: ", x)
        x_0 = g(x)
        i+=1
    print("iteraciones: ", i)
    print(x, 'con un error absoluto de: ', "{:3e}".format(abs(x-root1)))
    print('\nRaíz 2:')
    print("g(x)=ln(11x/2e)+1")
    g = lambda a:  math.log1p(-1+(11/2)*(a/math.e))+1
    x_0 = x_0_2 
    i=0
    x=0
    while abs(x-root2)>=0.00001:
        x = x_0
        print("x_0: ",x_0,"x: ", x)
        #if abs(g(x))>1:
        #    break
        x_0 = g(x)
        i+=1
    print("iteraciones: ", i)
    print(x, 'con un error absoluto de: ', "{:3e}".format(abs(x-root2)))


fixedPoint(.2, 2.7)