import math 
from statistics import mean
x=[18,25,3,41,5]
print(min(x))
print(max(x))
print(mean(x))

y=mean(x)

def closest(x, y):
      
    return x[min(range(len(x)), key = lambda i: abs(x[i]-y))]
      
# Driver code

print(closest(x,y))