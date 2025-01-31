"""
Let P4(x) = 2x^4 - 5x^3 - 11x^2 + 20^x + 10. Solve the following.

(a) Plot P4 over the interval [-3, 4].
(b) Find all zeros of P4, modifying Zeros-Polynomials-Newton-Horner.py, p.32.
(c) Add markers for the zeros to the plot.
(d) Find all roots of P4'(x) = 0.
(e) Add markers for the zeros of P4' to the plot.
"""

import numpy as np
import matplotlib.pyplot as plt

class poly:
    def __init__(self, name, coe=None): # this initialized a polynomial with a name
        self.name = name
        self.coe = coe      
          
    def assign_coefficients(self, new_coe):
        self.coe = new_coe[0]  # Remove the extra tuple nesting
        
    def evaluate(self, x):
        
        result = (self.coe[0] * x**4 + 
                 self.coe[1] * x**3 + 
                 self.coe[2] * x**2 + 
                 self.coe[3] * x + 
                 self.coe[4])
        return result
    
    def plot(self, start, end):
        x = np.linspace(start, end, 1000)
        y = self.evaluate(x)
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', label=self.name)
        plt.grid(True, alpha=0.3)
        plt.xlabel('x')
        plt.ylabel('P4(x)')
        plt.title(f'{self.name} over [{start}, {end}]')
        plt.legend()
        plt.show()

        # takes an input: A = [a_n, ..., a_0] 
        # produces the output: p,d = P(x0), DP(x0) = horner(A,x0)
def horner(A, x0):
    n = len(A)
    p = A[0]
    d = 0

    for i in range(1,n):
        d = p + x0*d
        p = A[i] + x0*p
    
    return p,d

def newton_horner(A, x0, tol, itmax):
    x = x0
    for it in range(1, itmax + 1):
        p,d = horner(A,x)
        h = -p/d
        x = x + h
        if(abs(h)<tol):
            break
    return x, it

polynomial4 = poly("Polynomial-4", None) # Initialized my new polynomial I called "Polynomial-4"
polynomial4.assign_coefficients([(2, -5, -11, 20, 10)]) #Assigned it whatever coefficients I want the coefficients 

"""
PART A
"""
polynomial4.plot(-3, 4) # Plot the polynomial over [-3, 4]

"""
PART B
"""
if __name__ == '__main__':
    
    tol = 10**(-12)
    itmax = 1000
    roots_array = []

    for x0 in [-2.5, -1,  1.5, 3]:

        x,it = newton_horner(polynomial4.coe,x0,tol,itmax)
        roots_array.append(x)
    print("For %f as the initial guess and %d iterations, the root found was %f"%(x0, it, x))


"""
PART C
"""


