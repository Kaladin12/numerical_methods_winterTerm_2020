import math

func = lambda x: 2*math.sin(x) - x**2
fp = lambda x : 2*math.cos(x)-2*x
g = lambda x: math.sqrt(2*math.sin(x))
X = 1.3

root = 1.404418240924343641

def biseccion(a,b,n):
    print("Bisección")
    aN = a
    bN = b
    for i in range(1,n+1):
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
    raiz =  (aN+bN)/2   
    if raiz != None:
        print("iteraciones: ", n)
        print(raiz, 'con un error absoluto de: ', "{:3e}".format(abs(root-raiz)))
    print("\n")

def newton(x_not, n):
    print("Newton-Raphson")
    for i in range(n):
        x = x_not - (func(x_not)/fp(x_not))
        print("x_i: "+str(x_not),"x: "+ str(x), "error: "+"{:3e}".format(abs(root-x)))
        x_not = x
    print("iteraciones: ", n)
    print(x,"con un error absoluto de: "+"{:3e}".format(abs(root-x)))
    print("\n")

def fixedPoint(x_i, n):
    print("Punto Fijo")
    print("función g(x)=(2*sin(x))^(1/2)")
    for i in range(n):
        x = x_i
        print("x: "+ str(x), "error: "+"{:3e}".format(abs(root-x)))
        x_i = g(x)
    print("iteraciones: ", n)
    print(x,"con un error absoluto de: "+"{:3e}".format(abs(root-x)))


biseccion(float(input('a: ')),float(input('b: ')), int(input('n: ')))
newton(1, 4)
fixedPoint(1, 5)
