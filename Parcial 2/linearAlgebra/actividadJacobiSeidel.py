import numpy as np
import math

def printJacobi():
    x_i = np.matrix('0;0;0')
    A = np.matrix('4 -1 1;4 -8 1;-2 1 5')
    b = np.matrix('7;-21;15')
    D = np.diag(np.diag(A))
    R = A-D
    Dinv = np.linalg.inv(np.diag(np.diag(A)))
    print("R:")
    print(R)
    print("D:")
    print(D)

def printGaussSeidel():
    x = np.matrix('0;0;0')
    A = np.matrix('4 -1 1;4 -8 1;-2 1 5')
    b = np.matrix('7;-21;15')
    D = np.diag(np.diag(A))
    L = np.tril(A)
    U = np.triu(A)-D
    DLinverse = np.linalg.inv(L)
    print("D")
    print(D)
    print("L")
    print(L-D)
    print("U")
    print(U)


def JacobiOne():
    print("Método de Jacobi")
    real = [2,4,3]
    x_i = np.matrix('0;0;0')
    A = np.matrix('4 -1 1;4 -8 1;-2 1 5')
    b = np.matrix('7;-21;15')
    D = np.diag(np.diag(A))
    R = A-D
    Dinv = np.linalg.inv(np.diag(np.diag(A)))
    error = 1
    i = 0
    while (error > 0.0001):
        x = Dinv*(b-R*x_i)
        x_i = x
        error = math.sqrt((x_i.item(0)-real[0])**2 + (x_i.item(1)-real[1])**2 + (x_i.item(2)-real[2])**2)
        print("x: ",x_i.item(0)," y: ",x_i.item(1), " z: ",x_i.item(2), " Error: ","{:3e}".format(error))
        i+=1
    print("Iteraciones: ", i)
    print("x:",x_i.item(0)," y:",x_i.item(1), " z:",x_i.item(2), "con un error absoluto de: ", error)

def GaussSeidelOne():
    print("\nMétodo de Gauss-Seidel")
    real = [2,4,3]
    x = np.matrix('0;0;0')
    A = np.matrix('4 -1 1;4 -8 1;-2 1 5')
    b = np.matrix('7;-21;15')
    D = np.diag(np.diag(A))
    L = np.tril(A)
    U = np.triu(A)-D
    DLinverse = np.linalg.inv(L)
    error = 1
    i = 0
    while (error > 0.0001):
        x = DLinverse*(b-U*x)
        error = math.sqrt((x.item(0)-real[0])**2 + (x.item(1)-real[1])**2 + (x.item(2)-real[2])**2)
        print("x: ",x.item(0)," y: ",x.item(1), " z: ",x.item(2), " Error: ","{:3e}".format(error))
        i+=1
    print("Iteraciones: ", i)
    print("x:",x.item(0)," y:",x.item(1), " z:",x.item(2), "con un error absoluto de: ", error)

JacobiOne()
GaussSeidelOne()
#printJacobi()
#printGaussSeidel()