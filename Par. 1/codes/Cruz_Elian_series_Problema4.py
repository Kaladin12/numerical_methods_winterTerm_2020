#Hecho por Elian Javier Cruz Esquivel

import math

realValue = 1.55088319692

coefficients = {
   "0": [[0,0]],
   "1": [[0,1], [1,0]],
   "2": [[0,2],[1,1],[2,0]],
   "3": [[0,3],[2,1],[1,2],[3,0]],
   "4": [[0,4],[1,3],[2,2],[3,1],[4,0]],
   "5": [[0,5],[1,4],[2,3],[3,2],[4,1],[5,0]],
   "6": [[0,6],[1,5],[2,4],[3,3],[4,2],[5,1],[6,0]]
}

sin = [] #coeficientes para la serie sin(x)
e = [] #coeficientes para la serie e^(x)

def eToX(x,n):
    S = 0
    for k in range(n):
       e.append(((x)**k)/(math.factorial(k)))

def sinX(x,n):
    S = 0
    for i in range(n):
        sin.append(0)
        signo = (-1)**i
        a = x**((2*i)+1)
        sin.append(signo*a / math.factorial((2*i)+1))

def eToXTimesSin():
    sinX(1,10)
    eToX(1,10)
    S = 0
    x = math.pi / 4
    for i in coefficients:
        partialSum = 0
        for j in coefficients[i]:
            #print(sin[j[0]]*e[j[1]])
            partialSum += e[j[0]]*sin[j[1]]
        S += partialSum * x**int(i)
        if abs(S-realValue)<=0.001:
            break
    print("\ne^x*sin(x) evaluado en",'\u03C0 / 4')
    print('Valor real: ',(math.e**x)*math.sin(x))
    print('Iteraciones :', i)
    print('Aprocimación: ', S, 'con un error de ', "{:2e}".format(abs((math.e**x)*math.sin(x) - S)))
    print('\n')

eToXTimesSin()