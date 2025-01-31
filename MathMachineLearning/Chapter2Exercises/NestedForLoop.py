"""
2.1 : Use Nested For loops to assign a 5x5 matrix A such that A[i,j] = ij
"""

import numpy as np

my_matrix = np.zeros((5,5), dtype='U2')  

for j in range(5):
    for i in range(5):
        my_matrix[i,j] = f"{i}{j}"  


print(my_matrix)

"""
Or, keeping the values as integers and not strings:
"""


my_int_matrix = np.zeros((5,5))

for i in range(5):
    for j in range(5):
        # Convert i and j to strings, concatenate them, then convert back to int
        my_int_matrix[i,j] = int(str(i) + str(j))

print(my_int_matrix)

