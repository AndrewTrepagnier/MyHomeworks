#Sorting algorithm is based on a script i once made with java converted over to python. 
import numpy as np

values = np.array(np.random.uniform(10, 20, 10))

n = len(values)

for j in range(n, 1, -1):
    for i in range(j - 1):
        if values[i] > values[i + 1]:
            tmp = values[i]
            values[i] = values[i + 1]
            values[i + 1] = tmp

print(values)
print(values[n-1])