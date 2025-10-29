# Creating 3D visualization of persistence zone in Navier–Stokes surrogate space
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define domain
nu_vals = np.linspace(0.01, 0.2, 200)  # viscosity ν
A0_vals = np.linspace(0.01, 2.0, 200)  # initial amplitude A₀
nu_grid, A0_grid = np.meshgrid(nu_vals, A0_vals)

# Define critical boundary A*(ν) = C * ν^{-α}
C = 0.5
alpha = 0.8
A_star = C * nu_vals**(-alpha)

# Create persistence and failure zones
zone = np.zeros_like(nu_grid)
for i in range(len(nu_vals)):
    zone[:, i] = A0_vals < A_star[i]  # 1 if regular (blue), 0 if failure (red)

# Create 3D surface for visualization
Z = zone.astype(float)  # 1.0 for regular, 0.0 for failure

# Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(nu_grid, A0_grid, Z, facecolors=np.where(Z > 0, 'blue', 'red'), rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)

# Plot critical boundary curve
ax.plot(nu_vals, A_star, zs=1.05, zdir='z', color='black', linewidth=2, label='Critical Boundary A*(ν)')

# Labels and title
ax.set_xlabel('Viscosity ν')
ax.set_ylabel('Initial Amplitude A₀')
ax.set_zlabel('Persistence Indicator')
ax.set_title('Persistence Zone in Navier–Stokes Surrogate Space')
ax.view_init(elev=30, azim=-60)
ax.legend()

# Save figure
import os
output_path = "/mnt/data/persistence_zone_3d.png"
if not os.path.exists("/mnt/data"):
    os.makedirs("/mnt/data")
plt.savefig(output_path)
plt.close()

print("3D visualization saved as 'persistence_zone_3d.png'")
