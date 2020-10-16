import math

def eToX(x,n):
    S = 0
    for k in range(n):
        S += ((x)**k)/(math.factorial(k))
    return S

def sinX(x,n):
    S = 0
    for i in range(n):
        signo = (-1)**i
        a = x**((2*i)+1)
        S =S + signo*a / math.factorial((2*i)+1)
    return S

x = float(input('valor de x: ')) * (math.pi / 180)
n = int(input("n: "))

S = sinX(x,n) * eToX(x,n)

print("{:3e}".format(abs(S-(math.e**x)*math.sin(x))))
print(S)

