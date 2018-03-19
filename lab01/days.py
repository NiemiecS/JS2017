#zad 2
import sys
from datetime import date
date1 = date.today()
date2 = date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
time_to = (date1 - date2)
print(time_to)