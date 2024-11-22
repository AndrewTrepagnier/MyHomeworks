import numpy as np

phi = 20 * np.pi/180
psi = 15 *np.pi/180
wt = 1.159e4
brg_ID = 55 * (1/25.4) # inch
S = 9.525 * (1/25.4)
print(S)

def W(wt):
    return (wt / np.cos(phi)*np.cos(psi))
def Wr(wt):
    return W(wt)*np.sin(phi)
def Wa(wt):
    return W(wt)*np.cos(phi)*np.sin(psi)
def R_bz(wt):
    return wt/2
def R_az(wt):
    return wt/2
def R_by(L):
    return (Wa(wt)*3.6235 + (Wr(wt)*((2*S+ 7.24 + L*(1/25.4))/2))) / (7.24+L)
def R_ay(L):
    return Wr(wt) - (Wa(wt)*3.6235 + (Wr(wt)*((2*S+7.24 + L*(1/25.4))/2))) / (7.24+L)
def R_ax(wt):
    return Wa(wt)


print(f"W is: ", W(wt))
print(f"Wr is: ", Wr(wt))
print(f"Wa is: ", Wa(wt))

def R_a_combine(L, wt):
    return ((R_ay(L)**2 + R_ax(wt)**2 + R_az(wt)**2))**(0.5)
def R_b_combine(L, wt):
    return ((R_by(L)**2  + R_bz(wt)**2))**(0.5)

for i in range(17, 65, 1):
    L = i 
    sum_y = R_by(L) + R_ay(L)

    print(f"The Rby value at L = {L} is {R_by(L)}")
    print(f"The Ray value at L = {L} is {R_ay(L)}")
    print(f"R_a combined is: {R_a_combine(L, wt)}")
    print(f"R_b combined is:  {R_b_combine(L, wt)}")
    print("------------------------------------------------")
    print("------------------------------------------------")

    print("Ra components")
    print(R_ax(wt))
    print(R_ay(17))
    print(R_az(wt))

    print("Rb components")
    #print(R_bx(wt))
    print(R_by(17))
    print(R_bz(wt))
    print(sum_y)
# BEARING LIFE CALCULATION:
# 21305cc

# Life = 25712.4 hrs
