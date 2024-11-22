import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, solve

m_dot = 41.75 #lbm/s
# Cpc_air = 0.2393125 #Btu/lbm*F interpolated in Table B-2 at 10F
# Cph_air = 0.24125 #Btu/lbm*F interpolated in Table B-2 at 72F
Cp_air = 0.24
A = 5000 #ft^2
T1 = 72
T2 = 10

Cpw = 1.0 #Btu/lbm*F
C_air = Cp_air*m_dot

def Cw(Q): #Cw is a function of flowrate
    return Cpw*Q*(8.34)*(1/60)



def Cmin(Q):# fucntion takes a flowrate and gives what the Cmin value is and the Cmin/Cmax ratio FOR THE FIRST EXCHANGER
    #Hot air heat exchanger,the first one it passes through , this exchanger gives the water he
    if C_air > Cw(Q):
        C_min = Cw(Q)
        return C_min
    else:
        C_min = C_air
        return C_min
# print(Cmin(100))

def U(Q):
    return 1/( (1/(13*(Q**0.8) + 0.047) ) )

def Overall_HT(Q):
    return (U(Q)*A) / NTU(Q)


def Cmax(Q):
    if C_air < Cw(Q):
        C_max = Cw(Q)
        return C_max
    else:
        C_max = C_air
        return C_max


def Heat_capacity(Q):
    return Cmin(Q)/Cmax(Q)

    
def NTU(Q):
    # NTU = UA/Cmin
    UA = U(Q) * A  # Using your U(Q) function and global A value
    return UA/Cmin(Q)

def effectiveness(Q): # Air mixed, water unmixed
    if C_air == Cmax(Q): # If this is true, use equation 11.33a
        e = (1/Heat_capacity(Q)) * (1 - np.exp(-Heat_capacity(Q)*(1-np.exp(-NTU(Q)))))
        
    elif Cw(Q) == Cmax(Q): # If this is true, use equation 11.34a
        e = 1 - np.exp(-(Heat_capacity(Q))**(-1) * (1-np.exp(-Heat_capacity(Q)*NTU(Q))))
    return e


def solve_heat_system(Q):
    # Get values from your existing functions
    cw = Cw(Q)
    cmin = Cmin(Q)
    e = effectiveness(Q)
    T1 = 72  
    T2 = 10 
    
    # Define symbolic variables
    heat, Th, Tc = symbols('heat Th Tc')
    
    # Define equations using your function values
    eq1 = heat - cw*(Th - Tc)
    eq2 = heat - e*cmin*(Th - T1)
    eq3 = heat - e*cmin*(T2 - Tc)
    
    # Solve system
    solution = solve((eq1, eq2, eq3), (heat, Th, Tc))

    
    # Print results
    print(f"\nResults for Q = {Q} gpm:")
    print(f"Heat transfer rate: {float(solution[heat]):.2f} BTU/hr")
    print(f"Hot outlet temp (Th): {float(solution[Th]):.2f} °F")
    print(f"Cold outlet temp (Tc): {float(solution[Tc]):.2f} °F")
    
    return {

        'heat': float(solution[heat]),
        'Th': float(solution[Th]),
        'Tc': float(solution[Tc])
    }

# Example usage
results = solve_heat_system(100)



    

