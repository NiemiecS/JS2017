#zad3
import sys

a= len (sys.argv)
tab = []
i=-1
for k in range (a):
	if len(sys.argv[k])>=3:
		tab.append(sys.argv[k])
		i = i + 1
print (i)
licznik = i 
tab2 = ' '
while licznik > 0:
	tab2 = tab2 +' '+ tab[licznik]
	licznik = licznik -1
print(tab2)