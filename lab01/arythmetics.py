#zad 1
import sys
print(sys.argv)
if (sys.argv[2]=='+'):
	print(int(sys.argv[1])+int(sys.argv[3]))
if (sys.argv[2]=='-'):\
	print(int(sys.argv[1])-int(sys.argv[3]))
if (sys.argv[2]=='*'):\
	print(int(sys.argv[1])*int(sys.argv[3]))
if (sys.argv[2]=='/'):\
	print(int(sys.argv[1])/int(sys.argv[3]))