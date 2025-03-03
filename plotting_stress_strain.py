import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# Set a nice style
sns.set_theme(style="whitegrid")

# Load the data
data_file = "stress_strain_for_py3.csv"
df = pd.read_csv(data_file)

# Find the ultimate tensile strength point (maximum stress)
max_stress_idx = df.iloc[:,0].idxmax()

# Trim the data to exclude points after the maximum stress (necking region)
df_trimmed = df.iloc[:max_stress_idx+1]

# Plot 1: Full stress-strain curve
plt.figure(figsize=(10, 6))
sns.lineplot(x=df.iloc[:,1], y=df.iloc[:,0], linewidth=2.5)
plt.scatter(df.iloc[:,1], df.iloc[:,0], s=30, alpha=0.6)
plt.title('Full Stress-Strain Curve', fontsize=14)
plt.xlabel('Strain (in/in)', fontsize=12)
plt.ylabel('Stress (psi)', fontsize=12)
plt.tight_layout()
plt.show()

# Plot 2: Trimmed stress-strain curve (up to UTS)
plt.figure(figsize=(10, 6))

# Plot the trimmed data
sns.lineplot(x=df_trimmed.iloc[:,1], y=df_trimmed.iloc[:,0], linewidth=2.5)
plt.scatter(df_trimmed.iloc[:,1], df_trimmed.iloc[:,0], s=30, alpha=0.6)

# Find and mark the ultimate tensile strength (endurance stress)
uts_stress = df_trimmed.iloc[:,0].max()
uts_strain = df_trimmed.iloc[max_stress_idx, 1]

# Manual specification of yield point based on your observation
# Find the closest point to strain=0.06 and stress=160000
target_strain = 0.06
target_stress = 160000
distances = np.sqrt((df_trimmed.iloc[:,1] - target_strain)**2 + 
                   ((df_trimmed.iloc[:,0] - target_stress)/target_stress*0.1)**2)  # Scale stress difference
yield_idx = distances.argmin()
yield_stress = df_trimmed.iloc[yield_idx, 0]
yield_strain = df_trimmed.iloc[yield_idx, 1]

# Mark the key points on the plot
plt.plot(uts_strain, uts_stress, 'ro', markersize=8)
plt.annotate(f'Ultimate Tensile Strength\n({uts_strain:.4f}, {uts_stress:.0f} psi)', 
             xy=(uts_strain, uts_stress), 
             xytext=(uts_strain+0.01, uts_stress*0.9),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
             fontsize=10)

plt.plot(yield_strain, yield_stress, 'go', markersize=8)
plt.annotate(f'Yield Strength\n({yield_strain:.4f}, {yield_stress:.0f} psi)', 
             xy=(yield_strain, yield_stress), 
             xytext=(yield_strain+0.02, yield_stress*0.7),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
             fontsize=10)

plt.title('Stress-Strain Curve with Key Points', fontsize=14)
plt.xlabel('Strain (in/in)', fontsize=12)
plt.ylabel('Stress (psi)', fontsize=12)
plt.tight_layout()
plt.show()

# Plot 3: Zoomed elastic region with linear fit
plt.figure(figsize=(10, 6))

# Use data up to the yield point for elastic region analysis
elastic_strain = df_trimmed.iloc[:yield_idx, 1]
elastic_stress = df_trimmed.iloc[:yield_idx, 0]

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(elastic_strain, elastic_stress)

# Create prediction line
x_line = np.array([0, max(elastic_strain)])
y_line = slope * x_line + intercept

# Plot elastic region data
sns.lineplot(x=elastic_strain, y=elastic_stress, linewidth=2.5)
plt.scatter(elastic_strain, elastic_stress, s=30, alpha=0.6)

# Plot the linear fit
plt.plot(x_line, y_line, 'r--', linewidth=2)

# Add equation to the plot
equation = f'σ = {slope:.2f}ε + {intercept:.2f}'
r_squared = f'R² = {r_value**2:.4f}'
young_modulus = f"Young's Modulus = {slope:.2f} psi"

plt.text(0.05, 0.85, equation, transform=plt.gca().transAxes, fontsize=12)
plt.text(0.05, 0.78, r_squared, transform=plt.gca().transAxes, fontsize=12)
plt.text(0.05, 0.71, young_modulus, transform=plt.gca().transAxes, fontsize=12)

plt.title('Elastic Region with Linear Fit', fontsize=14)
plt.xlabel('Strain (in/in)', fontsize=12)
plt.ylabel('Stress (psi)', fontsize=12)
plt.tight_layout()
plt.show()

