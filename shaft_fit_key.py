"""
VON MISES ALTERNATING AND MEAN STRESS USING STRESS CONCENTRATION FACTORS
"""

kt = 2.14
sig_a = kt*976.27*2 # kt of 2.4
sig_m = 0


kts = 3.0

tau_a = kts*3679.1*0
#tau_m = 5*tau_a
tau_m = kts*3679.1 

se = 15395.6
sut = 91e3

def von_mises_alt(sig_a, tau_a):

    return (sig_a**2 + 3*(tau_a**2))**(1/2)  

def von_mises_m(sig_m, tau_m):

    return (0 + 3*(tau_m**2))**(1/2) 


def nf(sig_a, tau_a):
    return ((von_mises_alt(sig_a, tau_a) / se) + von_mises_m(sig_m, tau_m) / sut)**-1


print("The von mises alternating is")
print(von_mises_alt(sig_a, tau_a))
print("The von mises mean is ")
print(von_mises_m(sig_m, tau_m))
print("The safety factor is:")
print(nf(sig_a, tau_a))
