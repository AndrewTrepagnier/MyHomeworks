import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Knowns that must first be defined
K = 1000
gc = 9.81
A = 1

f_f = 0.02
f_dw = 4*f_f 
L = 100
Di = 0.1

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





