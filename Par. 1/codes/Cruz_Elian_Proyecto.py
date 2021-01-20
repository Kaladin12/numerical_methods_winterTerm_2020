import math

func = lambda x: x**3 - 21
fp = lambda x : 3*x**2
g = lambda x: math.sqrt(21/x)
X = 1.3

root = 2.758924176

def biseccion(a,b):
    print("Bisección")
    aN = a
    bN = b
    i=0
    while abs((aN+bN)/2 - root)>0.0001:
        m_n = (aN+bN)/2
        f = func(m_n)
        print("a_N: "+str(aN),"b_N: "+str(bN),"m_N: "+str(m_n), "error: "+"{:3e}".format(abs(root-(aN+bN)/2 )))
        if func(aN)*f < 0:
            bN = m_n
        elif func(bN)*f < 0:
            aN = m_n
        elif f == 0:
            return m_n
        else:
            return None
        i+=1
    raiz =  (aN+bN)/2   
    if raiz != None:
        print("iteraciones: ", i)
        print(raiz, 'con un error absoluto de: ', "{:3e}".format(abs(root-raiz)))
    print("\n")

def newton(x_not):
    print("Newton-Raphson")
    i=0
    x=0
    while abs(root-x)>0.0001:
        x = x_not - (func(x_not)/fp(x_not))
        print("x_i: "+str(x_not),"x: "+ str(x), "error: "+"{:3e}".format(abs(root-x)))
        x_not = x
        i+=1
    print("iteraciones: ", i)
    print(x,"con un error absoluto de: "+"{:3e}".format(abs(root-x)))
    print("\n")

def fixedPoint(x_i):
    print("Punto Fijo")
    print("función g(x)=(27/x)")
    i=0
    x = 0
    while abs(root-x)>0.0001:
        x = x_i
        print("x: "+ str(x), "error: "+"{:3e}".format(abs(root-x)))
        x_i = g(x)
        i+=1
    print("iteraciones: ", i)
    print(x,"con un error absoluto de: "+"{:3e}".format(abs(root-x)))


#biseccion(2.8,3.5)
newton(2)
#fixedPoint(3.1)

def newtonCasa(x_not):
    root2 = 3.54559496319450
    print("\nNewton-Raphson")
    f = lambda a: 3*a**2 + (a**3)/2 - 60
    fD = lambda a: 6*a + (3/2)*a**2
    i=0
    x=0
    while abs(root2-x)>0.0001:
        x = x_not - (f(x_not)/fD(x_not))
        print("x_i: "+str(x_not),"x: "+ str(x), "error: "+"{:3e}".format(abs(root2-x)))
        x_not = x
        i+=1
    print("iteraciones: ", i)
    print(x,"con un error absoluto de: "+"{:3e}".format(abs(root2-x)))
    print("\n")
    print((0.5*x**3 + 3*x**2))

#newtonCasa(3)

def newtonCilindro(x_not):
    root2 = 2.85553455036179
    print("\nNewton-Raphson")
    f = lambda a: 2*math.pi*a**2 + (2/3)*math.pi*a**3 - 100
    fD = lambda a: 4*math.pi*a+2*math.pi*a**2
    i=0
    x=0
    while abs(root2-x)>0.0001:
        x = x_not - (f(x_not)/fD(x_not))
        print("x_i: "+str(x_not),"x: "+ str(x), "error: "+"{:3e}".format(abs(root2-x)))
        x_not = x
        i+=1
    print("iteraciones: ", i)
    print(x,"con un error absoluto de: "+"{:3e}".format(abs(root2-x)))
    print("\n")
    print(2*math.pi*x**2 + (2/3)*math.pi*x**3)

newtonCilindro(2)