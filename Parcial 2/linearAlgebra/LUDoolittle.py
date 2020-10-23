#Hecho por Elian Javier Cruz Esquivel

from numpy import *
import math


A = matrix("25 15 -5 -10;15 10 1 -7;-5 1 21 4;-10 -7 4 18")
b = matrix("0; 10; 76; 60")

n = 4
L = zeros((n,n))
U = zeros((n,n))


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
                    print( L.item((i,k)),U.item((k,j)))
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