import numpy as np
import math

def Jacobi(n):
    x_i = np.matrix('0;0;0')
    A = np.matrix('5 1 2;1 3 -1;1 2 4')
    b = np.matrix('13;4; 17')
    D = np.diag(np.diag(A))
    R = A-D
    D = np.linalg.inv(np.diag(np.diag(A)))
    #print(D,'\n',R,'\n', b)
    for i in range(n):
        x = D*(R*x_i+b)
        print("D: ",D)
        print("R: ",R)
        print("b: ",b)
        print("x: ",x,"\n")
        x_i = x
    print(x_i)

def GaussSeidelOne():
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
    print("\n")
    print("Iteraciones: ", i)
    print("x:",x.item(0)," y:",x.item(1), " z:",x.item(2), "con un error absoluto de: ", error)

def JacobiOne():
    real = [2,4,3]
    x_i = np.matrix('0;0;0')
    A = np.matrix('4 -1 1;4 -8 1;-2 1 5')
    b = np.matrix('7;-21;15')
    D = np.diag(np.diag(A))
    R = A-D
    Dinv = np.linalg.inv(np.diag(np.diag(A)))
    #print(D,'\n',R,'\n', b)
    error = 1
    i = 0
    while (error > 0.0001):
        x = Dinv*(b-R*x_i)
        x_i = x
        error = math.sqrt((x_i.item(0)-real[0])**2 + (x_i.item(1)-real[1])**2 + (x_i.item(2)-real[2])**2)
        print("x: ",x_i.item(0)," y: ",x_i.item(1), " z: ",x_i.item(2), " Error: ","{:3e}".format(error))
        i+=1
    print("\n")
    print("Iteraciones: ", i)
    print("x:",x_i.item(0)," y:",x_i.item(1), " z:",x_i.item(2), "con un error absoluto de: ", error)


def JacobiTwo(n,x_0, y_0, z_0):
    x_i = lambda a,b: (16-12*a-15*b)/10
    y_i = lambda a,b: (11-6*a-12*b)/8
    z_i = lambda a,b: (18-12*a-12*b)/18
    for i in range(n):
        x = x_i(y_0,z_0)
        y = y_i(x_0, z_0)
        z = z_i(x_0, y_0)
        x_0 = x
        y_0 = y
        z_0 = z
    print(x,y,z)


JacobiOne()
GaussSeidelOne()
JacobiTwo(10,0,0,0)