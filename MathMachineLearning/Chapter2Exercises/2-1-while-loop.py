"""
The variable d is initially equal to 1. Use a while loop to keep dividing d by 2 until
d < 10^-6.
(a) Determine how many divisions are made.
(b) Verify your result by algebraic derivation.

"""
import sympy as sp
import numpy as np
d = 1
division_counter = 0
while d>=1e-6: # Remember this is 10^-6
    print("Division Iteration: %i" %division_counter)
    print(d)
    d = d/2
    division_counter += 1
new_div = division_counter
print("It took %i iterations for d to become less than 10^-6" %new_div)

