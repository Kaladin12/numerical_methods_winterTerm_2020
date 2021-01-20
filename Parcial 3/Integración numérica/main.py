from trapecio import *
from simpsonThird import *
from simpsonThreeEights import *

#trapecio2([0,10.4,15,14.5,10.3,8.8,8.7,6.9,7.3,5.8,0],1.86,4,7.48)
#simpsonVect([0,10.4,15,14.5,10.3,8.8,8.7,6.9,7.3,5.8,0],1.86,4,7.48)

trapecio2([0,10,15,20,18,16,20,23,21,18,18,16,17,15,0],15,1,1)
simpsonVect([0,10,15,20,18,16,20,23,21,18,18,16,17,15,0],15,1,1)
#
#n=6
#print("n: ", n)
#print("Función: xln(x), [1,2]")
#
##1,a)
#f = lambda s: s*math.log1p(s-1)
#trapecio(1,2,n, 0.6362943611,f)
#simpson(n,1,2, 0.6362943611,f)
#simpson2(n,1,2, 0.6362943611,f)
#
#n=12
#print("n: ", n)
#print("Función: (x+2/x)^2 [1,2]")
###1,b)
#f = lambda v : (v+2/v)**2
#trapecio(1,2,n,8.333333333,f)
#simpson(n,1,2,8.333333333,f)
#simpson2(n,1,2,8.333333333,f) 
#
#n=18
#print("n: ", n)
#print("Función: x^2/(4-x^2)^.5 [-1,(3)^.5]")
###1,b)
#f = lambda v : (v**2)/(math.sqrt(4-v**2))
#trapecio(-1,math.sqrt(3),n,1.40954184602,f)
#simpson(n,-1,math.sqrt(3),1.40954184602,f)
#simpson2(n,-1,math.sqrt(3),1.40954184602,f) 
#
#
#n=10
#print("N: ", n)
#print("Función: 2/sqrt(1-x^2) [0,0.995]")
##1,b)
#f = lambda v : 2/math.sqrt((1-v**2))
#trapecio(0,0.995,n,math.pi,f)
#simpson(n,0,0.995,math.pi,f)
#simpson2(n,0,0.995,math.pi,f) 
#
#n=10
#print("N: ", n)
#print("Función: cos(x)/e^x [0,5pi/4]")
##1,b)
#b = (5/4)*math.pi
#f = lambda v : math.cos(v)/math.e**v
##trapecio(0,b,n,.5,f)
#simpson(n,0,b,.5,f) 
#simpson2(n,0,b,.5,f) 

#n=4
#print("n:", n)
#print("Función: sqrt(1+x^4) [0,2]")
#f = lambda v: math.sqrt(1+v**4)
#simpson(n, 0,2,3.6534,f)
#n=6
#print("n:", n)
#print("Función: sqrt(1+x^4) [0,2]")
#simpson2(n, 0,2,3.6534,f) 

#n=2
#print("n:", n)
#print("Función: sqrt(49-x^2) [0,1.854525089263916]")
#f = lambda v: 4*math.sqrt(49-v**2)#98*math.asin(v/7) + 2*v*math.sqrt(49-v**2)
#b =  1.854525089263916
#real = (49/3)*math.pi
#simpson(n,0,b,real,f) 
#n=3
#print("n:", n)
#simpson2(n,0,b,real,f) 

#f = lambda v: (1/math.cos(v))**3  #math.log1p(v-1)
#n=6
#simpson(n,0,math.pi/4,1.1477,f) 
#n = 6
#print("Función:  9pi/2 * sqrt(4+x^2) [0,2]")
#print("n:", n)
#f = lambda v: (9/2)*math.pi *(4-v**2)
#simpson(n, 0,2,24*math.pi,f)

#f = lambda v:6*math.sqrt(4-v**2)
#n=9
#print("Función: 6 sqrt(4+x^2) [0,2]")
#print("n:", n)
#simpson2(n,0,2,6*math.pi, f)

#f = lambda v: 2*(math.sqrt((16+5*v**2)/(4-v**2)))
#n = 20

#trapecio(0,1.99,n,15.8654395228,f)
#simpson(12,0,1.99,15.8654395228,f)

#f = lambda v: 3*math.pi* math.sqrt(16+5*v**2)
#n=6
#print("Función: 3pi sqrt(16+5x^2) [0,2]")
#print("n:", n)
#simpson(n,0,2,89.0007373719,f)