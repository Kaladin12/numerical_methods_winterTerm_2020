import math
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

def regressionGeneralized(n, x, y, isExp, isPot):
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
    print("a:",math.e**s.item(0))
    print("b:", s.item(1))
    xPlotter = [x.item(i) for i in range(np.prod(x.shape))]
    yPlotter = [y.item(i) for i in range(np.prod(y.shape))]
    newX = np.linspace(-25,100)#np.linspace(int(x.min())-1,int(x.max())+1)
    newY = 0
    if isExp==True:
        newY = math.e**(s.item(0)) * math.e**(newX*s.item(1))
        return [xPlotter, yPlotter,  newX, newY, s]

def generalizeExponential(n,x,y):
    yLn = np.log(y)   
    res = regressionGeneralized(n,x, yLn, True, False)
    yAsArray = [y.item(i) for i in range(np.prod(y.shape))]
    s = res[4]
    def error():
        error = 0
        getEstimation = lambda v: math.e**(s.item(0)) * math.e**(v*s.item(1))
        for i in range(n):
            result = (getEstimation(x.item(i))-y.item(i))
            error+=result
        print("error:", math.sqrt(error**2/n))
    error()
    plot(res[0], yAsArray, res[2], res[3], res[2].min()-1, res[3].min()-1, res[2].max()+1, res[3].max()+1)
    getEstimation = lambda v: math.e**(s.item(0)) * math.e**(v*s.item(1))
    print("Material despues de 50 semanas:",getEstimation(50))
    res = lambda v: math.log1p(v-1)
    getEstimationY = lambda v:(res(v) - res(math.e**s.item(0)))/s.item(1)
    print("Semanas para que queden 20 gramos de material:",getEstimationY(20))

def plot(xPlotter, yPlotter,x,y, minX,minY, maxX, maxY):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.axis([-20, 100, 0, 300])
    plt.plot(xPlotter, yPlotter, 'ro')
    plt.plot(x,y, 'b')
    plt.show()

x = matrix([0,1,2,3,4,5,6])
y = matrix([100,88.3,75.9,69.4,59.1,51.8,45.5])
generalizeExponential(2,x,y)
#(number of unknowns,x,y), 2-> lineal, exp, pot, 3->cuadratica
