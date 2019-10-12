import matplotlib.pyplot as plt
import numpy as np
import random

N = int(input())
print(N)
test = 1000
count=[0 for i in range(N+1)]             # Stores the count of the total occurrences

for t in range(test):
    X1 = 0
    X2 = 0
    X = [0 for i in range(0,N+1)]           # probability of X being there
    for i in range(0,N+1):
        val1 = random.randint(1,2)
        val2 = random.randint(1,2)
        if val1 is 1:
            # take step ahead
            X1 += 1
        else:
            X1 -= 1
        if val2 is 1:
            X2 += 1
        else:
            X2 -= 1
        if X1 is X2:
            X[i] = 1
    for j in range(0,N+1):
        count[j]+= X[j]

print(count)
Xaxis= [ i for i in range(N+1)]

plt.xlabel('Number of steps')
plt.ylabel('Probability of colliding')
plt.plot(Xaxis,count)
plt.show()
