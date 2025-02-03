"""
Let P4(x) = 2x^4 - 5x^3 - 11x^2 + 20^x + 10. Solve the following.

(a) Plot P4 over the interval [-3, 4].
(b) Find all zeros of P4, modifying Zeros-Polynomials-Newton-Horner.py, p.32.
(c) Add markers for the zeros to the plot.
(d) Find all roots of P4'(x) = 0.
(e) Add markers for the zeros of P4' to the plot.
"""
#By Andrew Trepagnier - alt658

import numpy as np
import matplotlib.pyplot as plt

class poly:
    def __init__(self, name, coe=None): # this initialized a polynomial with a name
        self.name = name
        self.coe = coe      
        self.roots = []  # Add roots attribute
          
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
        
        # Add markers for roots if they exist
        if self.roots:
            for root in self.roots:
                plt.plot(root, 0, 'ro', markersize=10)
        
        
        critical_points = all_minima_maxima(self)
        if critical_points:
            for cp in critical_points:
                plt.plot(cp, self.evaluate(cp), 'go', markersize=10, 
                        label='Critical Points')
        
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

def all_minima_maxima(polynomial):
    """Find all x values where P'(x) = 0 using Newton's method"""
    
    # Derivative coefficients using Horner
    deriv_coeffs = []
    for i in range(len(polynomial.coe)-1):
        deriv_coeffs.append(polynomial.coe[i] * (len(polynomial.coe)-i-1))
    
    minima_maxima = []
    #
    for x0 in [-2, 0, 2]:  # adjustable these starting points
        x, it = newton_horner(deriv_coeffs, x0, 10**(-12), 1000)
        if x not in minima_maxima:  # Avoid duplicates
            minima_maxima.append(x)
            print(f"Found critical point at x = {x}")
    
    return minima_maxima

#Defining an object of the class and assigning it coefficients using method:
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

    for x0 in [-2.5, -1,  1.5, 3]:
        x,it = newton_horner(polynomial4.coe,x0,tol,itmax)
        polynomial4.roots.append(x)
        print("For %f as the initial guess and %d iterations, the root found was %f"%(x0, it, x))

"""
PART C
"""
polynomial4.plot(-3, 4)  

"""
PART D
"""

# Example usage:
critical_points = all_minima_maxima(polynomial4)
polynomial4.plot(-3, 4)  


"""
PART E
"""

#See Plot

