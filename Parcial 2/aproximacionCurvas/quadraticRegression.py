import math
from numpy import *
import numpy as np
size = 7

x = matrix([-3,-2,-1,0,1,2,3])
y = matrix([7.5,3,0.5,1,3,6,14])

def quadraticReg():
    sumxSquared = 0
    sumx = 0
    sumxSquared = np.square(x).sum()
    sumxCube = np.power(x,3).sum()
    sumxFourth = np.power(x, 4).sum()
    n = size
    sumx = x.sum()
    sumy = y.sum()
    sumxTimesy = (x*np.transpose(y)).sum()
    sumxSquaredTimesy = (np.square(x)*np.transpose(y)).sum()
    A = matrix([[n, sumx,sumxSquared],[sumx, sumxSquared, sumxCube],[sumxSquared, sumxCube, sumxFourth]])
    print(A)
    r = matrix([[sumy],[sumxTimesy],[sumxSquaredTimesy]])
    print(np.linalg.inv(A)*r)

def linearRegresion():
    size = 4
    x = matrix([1,2,3,4])
    y = matrix([3,4,6,9])
    sumxSquared = 0
    sumx = 0
    sumxSquared = np.square(x).sum()
    n = size
    sumx = x.sum()
    sumy = y.sum()
    sumxTimesy = (x*np.transpose(y)).sum()
    A = matrix([[n, sumx],[sumx, sumxSquared]])
    S = matrix([[sumy],[sumxTimesy]]) 
    print(A,S, '\n')
    print(np.linalg.inv(A)*S)


def exponentialReg():
    size = 8
    x = matrix([1,2,5,15,25,30,35,40])
    y = matrix([99,95,85,55,30,24,20,15])
    n = size
    sumx = x.sum()
    sumxSquared = np.square(x).sum()
    sumLny = [math.log1p(y.item(i)-1) for i in range(n)]
    s= []
    for i in range(size):
        s.append(x.item(i)*sumLny[i])
    s = matrix(s).sum()
    A = matrix([[n, sumx],[sumx, sumxSquared]])
    S = matrix([[sum(sumLny)],[s]])
    result = np.linalg.inv(A)*S
    a = math.e**(result.item(0))
    b = result.item(1)
    xPlotter = [x.item(i) for i in range(n)]
    yPlotter = [y.item(i) for i in range(n)]
    newX = np.linspace(0,100)
    newY = a*math.e**(newX*b)
    print(a,b)
    plot(xPlotter, yPlotter, newX, newY)
quadraticReg()
