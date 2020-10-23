from numpy import *
import math


A = matrix("1 1 1 0 0 0;0 -1 0 1 -1 0; 0 0 -1 0 0 1; 0 10 -10 0 -15 -5;0 0 0 0 1 -1;5 -10 0 -20 0 0")
b = matrix("0; 0; 0; 0; 0; 200")

n = 6
L = zeros((n,n))
U = zeros((n,n))

def LU():
    for j in range(n):
        for i in range(n):
            if i <= j:
                s = A.item((i,j))
                for k in range(i):
                   s-=L.item((i,k))*U.item((k,j))
                U.itemset((i,j), s)
            if (j==i):
                L.itemset((i,i), 1)
            if (j<i):
                s = A.item((i,j))
                for k in range(j):
                    s -= L.item((i,k))*U.item((k,j))
                L.itemset((i,j),s/U.item((j,j)))

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