import math

#x = lambda a:(4/3)*math.pi*a**3 + 2*math.pi*a**2-60

#x =lambda a: (a + math.sqrt(a))*(20-a+math.sqrt(20-a))-120

x = lambda a: a**3-25
i=0
def biseccion(a,b,n):
    aN = a
    bN = b
  
    for i in range(n):
        m_n = aN+(-aN+bN)/2
        f = x(m_n)
        print(aN,bN,m_n)
        if x(aN)*f < 0:
            bN = m_n
        elif x(bN)*f < 0:
            aN = m_n
        elif f == 0:
            return m_n
        else:
            return None
    return (aN+bN)/2

raiz = biseccion(float(input('a: ')),float(input('b: ')), int(input('n: ')))       
if raiz != None:
    print(i)
    print(raiz, 'con un error absoluto de: ', "{:3e}".format(abs(25**(1/3)-raiz)))