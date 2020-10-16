from numpy import *
import math


A = matrix("1 1 1 0 0 0;0 -1 0 1 -1 0; 0 0 -1 0 0 1; 0 10 -10 0 -15 -5;0 0 0 0 1 -1;5 -10 0 -20 0 0")
b = matrix("0; 0; 0; 0; 0; 200")

n = int(input("Size: "))
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
                    L.itemset((i,j),L.item((i,j))-L.item((i,k))*U.item((k,j)))
                #print(L.item((i,j)),U.item((j,j)), i, j)
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
#LU()
print("L")
print(L)
print("U")
print(U)
Lyb()