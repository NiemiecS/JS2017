import sys
from math import sqrt
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
delta=(b**2)-(4*a*c)

if(delta>0):
	print(2)
	x1 = ( -b - sqrt(delta)) / (2*a)
	x2 = ( -b + sqrt(delta)) / (2*a)
	print(x1,x2)
if(delta==0):
	print(1)
	x=-b/(2*a)
	print(x)
if(delta<0):
	print("0")