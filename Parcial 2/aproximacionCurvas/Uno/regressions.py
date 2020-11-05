import math
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

def regressionGeneralized(n, x, y, isExp, isPot, isLn):
    A = zeros((n,n))
    b = zeros((n,1))
    xAsArray = [x.item(i) for i in range(np.prod(x.shape))]
    yAsArray = [y.item(i) for i in range(np.prod(y.shape))]
    def Afunc(last, i):
        for exp in range(n**2):
            if (exp%n==0 and exp!=0):
                last = exp-1-i
                i+=1
            aux = 0
            for x_i in xAsArray:
                aux += x_i**(exp - last)#
            A.itemset(exp, aux)
    def bfunc():
        for exp in range(n):
            temp = [(a**exp) * b for a, b in zip(xAsArray, yAsArray)]
            aux = sum(temp)
            b.itemset(exp, aux)
    Afunc(0,0)
    bfunc()
    s = np.matmul(np.linalg.inv(A),b)
    xPlotter = [x.item(i) for i in range(np.prod(x.shape))]
    yPlotter = [y.item(i) for i in range(np.prod(y.shape))]
    newX = np.linspace(-10,20)#np.linspace(int(x.min())-1,int(x.max())+1)
    newY = 0
    if isExp==True:
        a = math.e**s.item(0)
        b = s.item(1)
        print("a:",a)
        print("b:", b)
        newY = a*math.e**(newX*b)
        return [xPlotter, yPlotter,  newX, newY, s]
    elif isPot==True:
        print("a:",math.e**s.item(0))
        print("b:", s.item(1))
        newY = math.e**(s.item(0))*newX**(s.item(1))
        return [xPlotter, yPlotter,  newX, newY, s]
    elif isLn==True:
        print(s)
        res = np.zeros(len(newX))
        for i in range(len(newX)):
            res.itemset(i, math.log1p(newX.item(i)) )
        newY = s.item(0) + s.item(1)*res
        return [xPlotter, yPlotter, newX, newY, s]
    else:
        print("c:", s[0][0])
        print("b:", s[1][0])
        print("a:", s[2][0])
        for i in range(n):
            newY += newX**i*s.item(i)
        def error():
            answ = 0
            func = lambda v: s[0] + s[1]*v +s[2]*v**2
            for i in range(len(xAsArray)):
                answ += (func(xAsArray[i])-yAsArray[i])
            return math.sqrt(answ**2/len(xAsArray))
        print("error: ", error())
        highestX = -(s[1][0]/(2*s[2][0]))
        highestY = -((s[1][0])**2 / (4*s[2][0])) + s[0][0]
        print("Punto máximo: x:", highestX, "y:", highestY)
        #predY = lambda myX: s[1]*myX+s[0]
        #print("Para 4ft^2:",predY(4)[0],"dólares") #problema 1
        #predX = lambda myY: (myY-s[0])/s[1]
        #print("Para $6.5:",predX(6.5)[0], "ft^2") #problema 1
        plot(xPlotter, yPlotter, newX, newY, newX.min()-1, newY.min()-1, newX.max()+1, newY.max()+1)

def generalizeExponential(n,x,y):
    yLn = np.log(y)   
    res = regressionGeneralized(n,x, yLn, True, False, False)
    yAsArray = [y.item(i) for i in range(np.prod(y.shape))]
    xAsArray = [x.item(i) for i in range(np.prod(x.shape))]
    s = res[4]
    def error():
        error = 0
        getEstimation = lambda v: math.e**(s.item(0)) * math.e**(v*s.item(1))
        for i in range(len(yAsArray)):
            result = (getEstimation(xAsArray[i])-yAsArray[i])
            error+=result 
        print("error:", math.sqrt((error**2)/(len(yAsArray))))
    error()
    plot(res[0], yAsArray, res[2], res[3], res[2].min()-1, res[3].min()-1, res[2].max()+1, res[3].max()+1)
    getEstimation = lambda v: math.e**(s.item(0)) * math.e**(v*s.item(1))
    print("Para x=3, y=",getEstimation(3))
    res = lambda v: math.log1p(v-1)
    getEstimationY = lambda v:(res(v) - res(math.e**s.item(0)))/s.item(1)
    print("Para y=2500, x=",getEstimationY(2500))

def generalizedPot(n,x,y):
    xLn = np.log(x)
    yLn = np.log(y)
    res = regressionGeneralized(n,xLn, yLn, False, True, False)
    yAsArray = [y.item(i) for i in range(np.prod(y.shape))]
    xAsArray = [x.item(i) for i in range(np.prod(x.shape))]
    s = res[4]
    #print(res)
    getEstimation = lambda v: math.log1p(s.item(0)-1) *(v**s.item(1))
    print(getEstimation(3))
    plot(xAsArray, yAsArray, res[2], res[3], res[2].min()-1, res[3].min()-1, res[2].max()+1, res[3].max()+1)

def generalizedLog(n,x,y):
    yAsArray = [y.item(i) for i in range(np.prod(y.shape))]
    xAsArray = [x.item(i) for i in range(np.prod(x.shape))]
    print(len(xAsArray), len(yAsArray))
    xLn = np.log(x)
    res = regressionGeneralized(n, xLn, y, False, False, True)
    
    plot(xAsArray, yAsArray, res[2], res[3], res[2].min()-1, res[3].min()-1, res[2].max()+1, res[3].max()+1)

def plot(xPlotter, yPlotter,x,y, minX,minY, maxX, maxY):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.axis([-20,5,0,5000])
    plt.plot(xPlotter, yPlotter, 'ro')
    plt.plot(x,y, 'b')
    plt.show()


#x = matrix([1.7, 1.6, 2.8 ,5.6 ,1.3, 2.2, 1.3 ,1.1, 3.2 ,1.5 ,5.2, 4.6 ,5.8, 3.0])
#y = matrix([3.7, 3.9, 6.7, 9.5, 3.4, 5.6, 3.7, 2.7, 5.5, 2.9, 10.7, 7.6, 11.8, 4.1])
#r = regressionGeneralized(2,x,y, False, False, False)#(number of unknowns,x,y), 2-> lineal, exp, pot, 3->cuadratica

x = matrix([0, 0.108, 0.215, 0.322, 0.430, 0.537, 0.645, 0.752, 0.860])
y = matrix([1.037, 1.402, 1.638, 1.774, 1.803, 1.715, 1.509, 1.214, 0.831])
r = regressionGeneralized(3,x,y, False, False, False)#(number of unknowns,x,y), 2-> lineal, exp, pot, 3->cuadratica

#x = matrix([0.4, 0.8, 1.2, 1.6, 2, 2.5])
#y=matrix([805, 975, 1500, 1950, 2850, 3500])
#generalizeExponential(2, x,y)