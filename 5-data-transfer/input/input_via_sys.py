from math import exp
import sys
a,b,x = sys.argv[1],sys.argv[2],sys.argv[3]
y = float(a)*exp(float(b)*float(x))
print(y)