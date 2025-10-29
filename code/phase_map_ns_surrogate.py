# Generating phase map for Navier–Stokes surrogate regularity and failure zones
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Set plot style
plt.style.use('seaborn-v0_8')

# Define grid
nu_vals = np.linspace(0.01, 0.2, 300)
A0_vals = np.linspace(0, 2.0, 300)
nu_grid, A0_grid = np.meshgrid(nu_vals, A0_vals)

# Define critical boundary A*(ν) = C * ν^{-α}
C = 0.5
alpha = 0.8
A_star = C * nu_vals**(-alpha)

# Create mask: regular (A0 < A*(ν)) → blue, failure (A0 ≥ A*(ν)) → red
regular_mask = A0_grid < C * nu_grid**(-alpha)
failure_mask = ~regular_mask

# Create color map
phase_map = np.zeros_like(A0_grid)
phase_map[regular_mask] = 1  # blue
phase_map[failure_mask] = 2  # red
cmap = ListedColormap(['white', 'blue', 'red'])

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(phase_map, extent=[nu_vals.min(), nu_vals.max(), A0_vals.min(), A0_vals.max()],
               origin='lower', aspect='auto', cmap=cmap)

# Overlay critical boundary
ax.plot(nu_vals, A_star, 'k--', linewidth=2, label=r'$A^*(\nu) = C\nu^{-\alpha}$')

# Labels and title
ax.set_xlabel('Viscosity ν', fontsize=12)
ax.set_ylabel('Initial Amplitude $A_0$', fontsize=12)
ax.set_title('Phase Map of Regularity and Failure Zones', fontsize=14)
ax.legend()

# Save figure
output_path = "/mnt/data/phase_map_ns_surrogate.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print("Phase map saved as:", output_path)
