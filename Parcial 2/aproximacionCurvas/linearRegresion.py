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
    print(s)
    xPlotter = [x.item(i) for i in range(np.prod(x.shape))]
    yPlotter = [y.item(i) for i in range(np.prod(y.shape))]
    newX = np.linspace(-25,100)#np.linspace(int(x.min())-1,int(x.max())+1)
    newY = 0
    if isExp==True:
        newY = math.e**(s.item(0)) * math.e**(newX*s.item(1))
        return [xPlotter, yPlotter,  newX, newY, s]
    elif isPot==True:
        newY = math.e**(s.item(0))*newX**(s.item(1))
        return [xPlotter, yPlotter,  newX, newY, s]
    else:
        for i in range(n):
            newY += newX**i*s.item(i)
        plot(xPlotter, yPlotter, newX, newY, newX.min()-1, newY.min()-1, newX.max()+1, newY.max()+1)

def generalizeExponential(n,x,y):
    yLn = np.log(y)   
    res = regressionGeneralized(n,x, yLn, True, False)
    yAsArray = [y.item(i) for i in range(np.prod(y.shape))]
    s = res[4]
    plot(res[0], yAsArray, res[2], res[3], res[2].min()-1, res[3].min()-1, res[2].max()+1, res[3].max()+1)
    getEstimation = lambda v: math.e**(s.item(0)) * math.e**(v*s.item(1))
    print(getEstimation(50))

def generalizedPot(n,x,y):
    xLn = np.log(x)
    yLn = np.log(y)
    res = regressionGeneralized(n,xLn, yLn, False, True)
    yAsArray = [y.item(i) for i in range(np.prod(y.shape))]
    xAsArray = [x.item(i) for i in range(np.prod(x.shape))]
    s = res[4]
    print(res)
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
    plt.axis([minX, maxX, minY, maxY])
    plt.plot(xPlotter, yPlotter, 'ro')
    plt.plot(x,y, 'b')
    plt.show()

#linearRegresion()
#exponentialReg()
#x = matrix([1,2,3,4])
#y = matrix([3,4,6,9])
#x = matrix([-3,-2,-1,0,1,2,3])
#y = matrix([7.5,3,0.5,1,3,6,14])
#x = matrix([1,2,5,15,25,30,35,40])
#y = matrix([99,95,85,55,30,24,20,15])
#y = generalizeExponential(2,x,y)
#regressionGeneralized(2, x,y)
x = matrix([10,20,30,40,50,60,70,80])
y = matrix([1.03,1.33,1.52,1.68,1.81,1.91,2.01,2.11])
generalizedPot(2,x,y)
