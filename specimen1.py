import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#INITIALIZED PARAMETERS ===============================
file_path = '/Users/andrewtrepagnier/.cursor-tutor/projects/solid_mechanics/Stress-Strain-Data/Specimen_1.csv'
diameter = 0.5  # diameter in inches
length = 2.0    # length in inches
#======================================================

# Calculate cross-sectional area in square inches
area = 3.14159 * (diameter/2)**2  # area of a circle in square inches

# Read the data
data = pd.read_csv(file_path, header=0, skiprows=[1])
force = data['Force'].astype(float) 
displacement = data['Displacement'].astype(float) 

# Calculate stress (psi) and strain
stress = force / area  # stress = force/area (in psi)
strain = displacement / length  # strain = change in length/original length
toughness = np.trapz(stress, strain) #Integrate under plot with trapozoidal rule for toughness

print(f"Toughness: {toughness} PSI")
print(f"Maximum stress: {stress.max():.2f} psi")
print(f"Maximum strain: {strain.max():.2f}")


plt.figure(figsize=(10, 6))
plt.plot(strain, stress, 'b-', linewidth=2)
plt.xlabel('Strain')
plt.ylabel('Stress (psi)')
plt.title('Stress-Strain Curve')
plt.grid(True)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.tight_layout()
plt.show()







