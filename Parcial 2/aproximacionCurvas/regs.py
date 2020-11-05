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
    newX = np.linspace(0,75, 1001)#np.linspace(int(x.min())-1,int(x.max())+1)
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
        a = s.item(0)
        b = s.item(1)
        print("a:",a)
        print("b:", b)
        res = np.zeros(len(newX))
        for i in range(len(newX)):
            res.itemset(i, math.log1p(newX.item(i)) )
        newY = s.item(0) + s.item(1)*res
        return [xPlotter, yPlotter, newX, newY, s]
    else:
        for i in range(n):
            newY += newX**i*s.item(i)
        print("a:", s[3][0], "b:", s[2][0], "c:", s[1][0], "d:", s[0][0] ) 
        print("La ecuación es:",str(s[3][0])+"x^3"+str(s[2][0])+"x^2+"+str(s[1][0])+"x+"+str(s[0][0]))
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
    print("Para S=20, N=",getEstimation(20))

def generalizedPot(n,x,y):
    xLn = np.log(x)
    yLn = np.log(y)
    res = regressionGeneralized(n,xLn, yLn, False, True, False)
    yAsArray = [y.item(i) for i in range(np.prod(y.shape))]
    xAsArray = [x.item(i) for i in range(np.prod(x.shape))]
    s = res[4]
    getEstimation = lambda v: math.e**s.item(0) *(v**s.item(1))
    def error():
        error = 0
        for i in range(len(yAsArray)):
            result = (getEstimation(xAsArray[i])-yAsArray[i])
            error+=result 
        print("error:", math.sqrt((error**2)/(len(yAsArray))))
    error()
    print("Para S=20, N=",getEstimation(20))
    plot(xAsArray, yAsArray, res[2], res[3], res[2].min()-1, res[3].min()-1, res[2].max()+1, res[3].max()+1)

def generalizedLog(n,x,y):
    yAsArray = [y.item(i) for i in range(np.prod(y.shape))]
    xAsArray = [x.item(i) for i in range(np.prod(x.shape))]
    xLn = np.log(x)
    res = regressionGeneralized(n, xLn, y, False, False, True)
    s=res[4]
    getEstimation = lambda v:res[4][0] + res[4][1]*math.log1p(v-1)
    def error():
        error = 0
        for i in range(len(yAsArray)):
            result = (getEstimation(xAsArray[i])-yAsArray[i])
            error+=result 
        print("error:", math.sqrt((error**2)/(len(yAsArray))))
    error()
    print("Para S=20, N=",getEstimation(20))
    plot(xAsArray, yAsArray, res[2], res[3], res[2].min()-1, res[3].min()-1, res[2].max()+1, res[3].max()+1)

def plot(xPlotter, yPlotter,x,y, minX,minY, maxX, maxY):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    plt.axis([0,75,0,50])
    plt.plot(xPlotter, yPlotter, 'ro')
    plt.plot(x,y, 'b')
    plt.show()



x = matrix([1,2,3,4])
y = matrix([1,1,2,6])
r = regressionGeneralized(4,x,y, False, False, False)
#x = matrix([1,2,4,8,16,32,64])
#y = matrix([2,4,7,11,16,19,21])
#generalizedPot(2,x,y)
#generalizedLog(2, x,y)