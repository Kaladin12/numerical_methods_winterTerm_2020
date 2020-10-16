Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 0
>>> import math
>>> for i in range(10):
	x+=1/math.factorial(i)

	
>>> x
2.7182815255731922
>>> x = 0
>>> for i in range(1000):
	x+=1/math.factorial(i)

	
>>> x
2.7182818284590455
>>> math.abs(math.e - x)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    math.abs(math.e - x)
AttributeError: module 'math' has no attribute 'abs'
>>> x = 0
>>> for i in range(1000):
	x+=2**i/math.factorial(i)

	
>>> 
>>> x
7.389056098930649
>>> x=0
>>> for i in range(10):
	x+=2**i/math.factorial(i)

	
>>> x
7.3887125220458545
>>> x=0
>>> for i in range(1000):
	x+=((-1)**k) / math.factorial(i)

	
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    x+=((-1)**k) / math.factorial(i)
NameError: name 'k' is not defined
>>> for i in range(1000):
	x+=((-1)**i) / math.factorial(i)

	
>>> x
0.36787944117144245
>>> x*4
1.4715177646857698
>>> x=0
>>> for i in range(1000):
	x+=((-1)**i)/(2*k+1)

	
Traceback (most recent call last):
  File "<pyshell#31>", line 2, in <module>
    x+=((-1)**i)/(2*k+1)
NameError: name 'k' is not defined
>>> for i in range(1000):
	x+=((-1)**i)/(2*i+1)

	
>>> x
0.7851481634599485
>>> 4*x
3.140592653839794
>>> math.pi
3.141592653589793
>>> x=0
>>> for i in range(10000000):
	x+=((-1)**i)/(2*i+1)

	
>>> 4*x
3.1415925535897915
>>> 