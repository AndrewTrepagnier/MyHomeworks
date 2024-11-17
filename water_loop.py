import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Knowns that must first be defined
abs_rough = 0.02 #ft
viscosity = 6.58e-4  #lbm/ft/s
rho = 62.3 #lbm/ft^3

K = 1000
gc = 32.2 #lbm*ft/lbf*s^2
g = 32.2 #ft/s^2


f_f = 0.02
f_dw = 4*f_f 
L = 100
Di = 0.1722 #ft for 2" sch 40 pipe

rel_rough = abs_rough/Di
A = np.pi*(Di/2)**2 #ft^2

#functions 
def hf_minor(Q):
    return K*(Q**2)/(2*gc*A**2)

def hf_major(Q):
    return f_dw*(L/Di)*(Q**2)/(2*gc*A**2)

def hx_losses(Q):
    return 0.0049*Q**1.852

def total_head_loss(Q): # total head loss is dependent on Q alone
    return hf_minor(Q) + hf_major(Q) + 2*hx_losses(Q) #2*hx_losses because there are two heat exchangers

def overall_ht_coeff(Q): #Big U
    return ( 1/(13*Q**0.8) +0.047)**-1
def reynolds_number(Q):
    return (4*Q*rho)/(np.pi*Di*viscosity) # viscoisty is kinematic viscosity

#function with embedded conditional for determining what the fricton factor will be
def friction_factor(Q):
    if reynolds_number(Q) >= 2300:
        f_f = (0.3086)/(np.log10(6.9/reynolds_number(Q) + (rel_rough/(3.7*Di))**1.11))**2
    elif reynolds_number(Q) < 2300:
        f_f = 64/reynolds_number(Q)
    else:
        print("Reynolds number is out of range")
    return f_f
#function for calculating the friction factor for turbulent flow
def f_t(Q):
    return 0.3086/(np.log10((rel_rough/3.7*Di)**1.11))**2





