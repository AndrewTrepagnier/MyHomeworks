import numpy as np

Tfilm = []
rey = []
Nu = []
hfm = []

#Recorded expiremental data
Ua = [0.98, 2.99, 4.99, 6.97]
Uc = [1.22 * u for u in Ua]  # Convert each element individually
T9 = [23.3, 24.0, 24.3, 24.7]
Tsurf= [444, 378, 298, 250]
Volt = [19.5, 20.0, 24.3, 19.7]
Current = [3.50, 3.62, 3.4, 3.40]


for i in range(len(T9)):
    Tfilm = (Tsurf[i] + T9[i])  / 2 + 273
    print(Tfilm)

# Hand Calculated the Interpolated K and Pr Values below
k = [0.040808, 0.038658, 0.03598, 0.03435]
Pr = [0.680, 0.68156, 0.6849, 0.68775]
visc = [v * 10**(-5) for v in [3.876, 3.468, 2.987, 2.710]]  # m^2/s



A1 = np.pi*0.01*0.07

def Qf(Hf_m, A1, Tsurf, Ta): # Ta will be T9 in this instance
    return Hf_m*A1*(Tsurf - Ta)

def Qr(Hr_m, A1, Tsurf, Ta):
    return Hr_m*A1*(Tsurf - Ta)

def Hr_m(Ts, Ta):
    return 0.95*56.7*10**(-9)*((Ts**4 - Ta**4) / (Ts - Ta))

def reynolds(Uc, visc):
    for i in range(len(Uc)):
        rey.append(Uc[i]*0.01 / visc[i])
    return rey

def Nusselt(rey, Pr):
    Nu = []
    for k in range(len(rey)):
        # Break down the equation into parts for clarity
        numerator = 0.62 * (rey[k]**0.5) * (Pr[k]**0.33)
        denominator = (1 + (0.4/Pr[k])**0.66)**0.25
        reynolds_term = 1 + (rey[k]/282000)**0.5
        
        # Complete Nusselt equation
        nu_ = 0.3 + (numerator/denominator) * reynolds_term
        Nu.append(nu_)
    return Nu


def Hfm_(k, Nu):
    for j in range(len(k)):
        hfm.append((k[j]/0.01) * Nu[j])
    return hfm


#First) Calculate Reynolds with Uc and visc parameters
#second) Calculate Nusselt with new rey array and known Pr parameters
#third) Calculate Hrm with Tsurf and T9
#fourth) Calculate Hfm with k and Nu as inputs

#fifth) Calculate Qf using hfm, A1, Tsurf, and T9
# sixth) Calculate Qr with Hr_m(Tsurf, T9) , A1, Tsurf, and T9 as parameters

# First) Calculate Reynolds with Uc and visc parameters
rey = reynolds(Uc, visc)
print("\nReynolds numbers:")
for i, r in enumerate(rey):
    print(f"Rey_{i+1}: {r:.2f}")

# Second) Calculate Nusselt with new rey array and known Pr parameters
Nu = Nusselt(rey, Pr)
print("\nNusselt numbers:")
for i, nu in enumerate(Nu):
    print(f"Nu_{i+1}: {nu:.2f}")

# Third) Calculate Hrm with Tsurf and T9
hrm_values = []
for i in range(len(T9)):
    Ts = Tsurf[i] + 273  # Convert to Kelvin
    Ta = T9[i] + 273     # Convert to Kelvin
    hrm = Hr_m(Ts, Ta)
    hrm_values.append(hrm)
print("\nHr_m values:")
for i, h in enumerate(hrm_values):
    print(f"Hr_m_{i+1}: {h:.2f} W/m²K")

# Fourth) Calculate Hfm with k and Nu as inputs
hfm = Hfm_(k, Nu)
print("\nHfm values:")
for i, h in enumerate(hfm):
    print(f"Hfm_{i+1}: {h:.2f} W/m²K")

# Fifth) Calculate Qf using hfm, A1, Tsurf, and T9
Qf_values = []
for i in range(len(T9)):
    qf = Qf(hfm[i], A1, Tsurf[i], T9[i])
    Qf_values.append(qf)
print("\nQf values:")
for i, q in enumerate(Qf_values):
    print(f"Qf_{i+1}: {q:.2f} W")

# Sixth) Calculate Qr with Hr_m(Tsurf, T9), A1, Tsurf, and T9
Qr_values = []
for i in range(len(T9)):
    qr = Qr(hrm_values[i], A1, Tsurf[i], T9[i])
    Qr_values.append(qr)
print("\nQr values:")
for i, q in enumerate(Qr_values):
    print(f"Qr_{i+1}: {q:.2f} W")

print(Ua)
