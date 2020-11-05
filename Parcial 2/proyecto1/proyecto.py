import math
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

def JacobiOne():
    print("Método de Jacobi")
    x_i = np.matrix([[0],[2],[1],[1]])
    A = np.matrix([[4,-1,1,0],[4,-8,1,2],[-2,1,5,-1],[1,-4,3,10]])
    b = np.matrix([[7],[-23],[16],[-15]])
    D = np.diag(np.diag(A)) 
    Dinv = np.linalg.inv(np.diag(np.diag(A)))
    R = A-D
    def printJacobi():
        print("R:")
        print(R)
        print("D:")
        print(D)
    printJacobi()
    real = [2,4,3,-1]
    error = 1
    for i in range(15):
        x = Dinv*(b-R*x_i)
        x_i = x
        error = math.sqrt((x_i.item(0)-real[0])**2 + (x_i.item(1)-real[1])**2 + (x_i.item(2)-real[2])**2+ (x_i.item(3)-real[3])**2)
        print("a: ",x_i.item(0)," b: ",x_i.item(1), " c: ",x_i.item(2), " d: ",x_i.item(3), " Error: ","{:3e}".format(error))
    print("Iteraciones: ", i)
    print("a:",x_i.item(0)," b:",x_i.item(1), " c:",x_i.item(2), " d:",x_i.item(3), "con un error absoluto de: ", error)

def GaussSeidelOne():    
    x = np.matrix([[0],[2],[1],[1]])
    A = np.matrix([[4,-1,1,0],[4,-8,1,2],[-2,1,5,-1],[1,-4,3,10]])
    b = np.matrix([[7],[-23],[16],[-15]])
    D = np.diag(np.diag(A))
    L = np.tril(A)
    U = np.triu(A)-D
    DLinverse = np.linalg.inv(L)
    print("\nMétodo de Gauss-Seidel")
    def printGaussSeidel():
        print("D")
        print(D)
        print("L")
        print(L-D)
        print("U")
        print(U)
    printGaussSeidel()
    real = [2,4,3,-1]
    error = 1
    for i in range(15):
        x = DLinverse*(b-U*x)
        error = math.sqrt((x.item(0)-real[0])**2 + (x.item(1)-real[1])**2 + (x.item(2)-real[2])**2+ (x.item(3)-real[3])**2)
        print("a: ",x.item(0)," b: ",x.item(1), " c: ",x.item(2), " d: ",x.item(3), " Error: ","{:3e}".format(error))
    print("Iteraciones: ", i)
    print("a:",x.item(0)," b:",x.item(1), " c:",x.item(2), " d:",x.item(3), "con un error absoluto de: ", error)

def TwoLU():
    n=3
    A = np.matrix([[1/10,1/4,1/20],[1/7.5,1/6,1/15],[1/15,1/3,1/40]])
    b = np.matrix([[2.5],[3],[1.75]])
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    def LU():
        for j in range(n):
            for i in range(n):
                if i <= j:
                    U.itemset((i,j),A.item((i,j)))
                    for k in range(i):
                        U.itemset((i,j),U.item((i,j))-L.item((i,k))*U.item((k,j)))
                if (j<=i):
                    L.itemset((i,j),A.item((i,j)))
                    for k in range(j):
                        L.itemset((i,j),L.item((i,j))-L.item((i,k))*U.item((k,j)))
                    L.itemset((i,j),L.item((i,j))/U.item((j,j)))

    def Lyb(): 
        y = [0 for _ in range(n)]
        x = [0 for _ in range(n)]
        for i in range(n):
            res = b.item(i)
            for j in range(n):
                res -= y[j]*L.item((i,j))
            y[i] = res  
        k = 0
        for i in range(n-1,-1,-1):
            res = y[i]
            for j in range(n-k,n):
                res -= x[j]*U.item((i,j))
                #print(x[j],U.item((i,j)))
            x[i] = res/U.item((i,i))
            k+=1
        print("y")
        print(y)
        print("x")
        print(x)
    LU()
    print("L")
    print(L)
    print("U")
    print(U)
    Lyb()



#JacobiOne()
#GaussSeidelOne()
TwoLU()
print()