import math

x = math.pi / 4
real = math.sin(2*x)

def serie():
    i = 0
    S = 0
    while abs(S-real)>0.00001:
        S += (-1)**i * (2**(2*i+1) * (x**(2*i+1))) / math.factorial(2*i + 1)
        print(S)
        i+=1
    print(S, i)

def newtonA(x_0):
    root = 0.517757363682458
    print("\nNewton-Raphson")
    f = lambda a: a*math.e**a - math.cos(a)
    fD = lambda a: (math.e**a)*(a+1) + math.sin(a)
    i=0
    x=0
    while abs(root-x)>=0.0001:
        x = x_0 - (f(x_0)/fD(x_0))
        print("x_i: "+str(x_0),"x: "+ str(x), "error: "+"{:3e}".format(abs(root-x)))
        x_0 = x
        i+=1
    print("iteraciones: ", i)
    print(x,"con un error absoluto de: "+"{:3e}".format(abs(root-x)))
    print("\n")

def newtonB(x_0, x_0_2):
    root = 0.0538775
    root2 = 2.93851
    print("\nNewton-Raphson")
    f = lambda a: 4**a -20*a
    fD = lambda a: math.log1p(3)*4**a - 20
    i=0
    x=0
    print("Raíz 1:")
    while abs(root-x)>=0.0001:
        x = x_0 - (f(x_0)/fD(x_0))
        print("x_i: "+str(x_0),"x: "+ str(x), "error: "+"{:3e}".format(abs(root-x)))
        x_0 = x
        i+=1
    print("iteraciones: ", i)
    print(x,"con un error absoluto de: "+"{:3e}".format(abs(root-x)))
    print("\n")
    i=0
    x=0
    x_0 = x_0_2
    print("Raíz 2:")
    while abs(root2-x)>=0.0001:
        x = x_0 - (f(x_0)/fD(x_0))
        print("x_i: "+str(x_0),"x: "+ str(x), "error: "+"{:3e}".format(abs(root2-x)))
        x_0 = x
        i+=1
    print("iteraciones: ", i)
    print(x,"con un error absoluto de: "+"{:3e}".format(abs(root2-x)))
    print("\n")

def biseccionA(a,b):
    root = 0.517757363682458
    func = lambda a: a*math.e**a - math.cos(a)
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

def biseccionB(a,b,a2,b2):
    root = 0.0538775
    root2 = 2.93851
    func = lambda a:  4**a -20*a
    print("Bisección")
    aN = a
    bN = b
    i=0
    print("Raíz 1: ")
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

    aN = a2
    bN = b2
    raiz = 0
    i=0
    print("Raíz 1: ")
    while abs((aN+bN)/2 - root2)>0.0001:
        m_n = (aN+bN)/2
        f = func(m_n)
        print("a_N: "+str(aN),"b_N: "+str(bN),"m_N: "+str(m_n), "error: "+"{:3e}".format(abs(root2-(aN+bN)/2 )))
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
        print(raiz, 'con un error absoluto de: ', "{:3e}".format(abs(root2-raiz)))
    print("\n")

def fixedPointA(x_i):
    g = lambda a: math.cos(a) / math.e**a 
    root = 0.517757363682458
    print("Punto Fijo")
    print("función g(x)=")
    i=0
    x = 0
    while abs(root-x)>0.0001:
        x = x_i
        print("x: "+ str(x), "error: "+"{:3e}".format(abs(root-x)))
        x_i = g(x)
        i+=1
    print("iteraciones: ", i)
    print(x,"con un error absoluto de: "+"{:3e}".format(abs(root-x)))

def fixedPointB(x_i, x_i_2):
    root = 0.0538775
    root2 = 2.93851
    g = lambda a: 4**a / 20
    print("Punto Fijo")
    print("función g(x)=")
    i=0
    x = 0
    while abs(root-x)>0.0001:
        x = x_i
        print("x: "+ str(x), "error: "+"{:3e}".format(abs(root-x)))
        x_i = g(x)
        i+=1
    print("iteraciones: ", i)
    print(x,"con un error absoluto de: "+"{:3e}".format(abs(root-x)), '\n')
    
    g = lambda a: math.log(20*a,4)
    x_i = x_i_2
    i=0
    x = 0
    while abs(root2-x)>0.0001:
        x = x_i
        print("x: "+ str(x), "error: "+"{:3e}".format(abs(root2-x)))
        x_i = g(x)
        i+=1
    print("iteraciones: ", i)
    print(x,"con un error absoluto de: "+"{:3e}".format(abs(root2-x)), '\n')

#serie()
#newtonA(0.25)
#newtonB(0.5, 2.5)
#biseccionA(0,2)
#biseccionB(0,1,2,3)
#fixedPointA(0)
fixedPointB(0,2.6)