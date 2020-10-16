from numpy import *
import math


A = matrix("10 12 15;6 8 12;12 12 18")
b = matrix("960 660 1080")

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