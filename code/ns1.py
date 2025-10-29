# Generating phase map for regularity detection in 3D Navier–Stokes surrogate
import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
os.makedirs("/mnt/data", exist_ok=True)

# Define viscosity and amplitude values
nu_values = np.array([1e-7, 2e-7, 5e-7, 1e-6, 2e-6, 5e-6, 1e-5])
A0_values = np.array([2.5, 2.7, 2.9, 3.1, 3.3, 3.5])

# Create a grid for phase map
phase_map = np.zeros((len(A0_values), len(nu_values)))

# Fill phase map based on failure conditions
for j, nu in enumerate(nu_values):
    if nu == 1e-7:
        failure_threshold = 2.7
    elif nu == 2e-7:
        failure_threshold = 2.9
    elif nu == 5e-7:
        failure_threshold = 3.1
    elif nu == 1e-6:
        failure_threshold = 3.3
    elif nu >= 2e-6:
        failure_threshold = 10.0  # No failure observed
    for i, A0 in enumerate(A0_values):
        phase_map[i, j] = 1 if A0 >= failure_threshold else 0  # 1 = failure, 0 = regularity

# Plotting
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(8, 5))
cmap = plt.cm.get_cmap('bwr', 2)  # blue for 0, red for 1

c = ax.imshow(phase_map, origin='lower', aspect='auto', cmap=cmap,
              extent=[nu_values[0], nu_values[-1], A0_values[0], A0_values[-1]])

# Overlay estimated critical line A*(nu)
critical_A = [2.7, 2.9, 3.1, 3.3, 3.5, 3.5, 3.5]
ax.plot(nu_values, critical_A, color='black', linestyle='--', linewidth=2, label='Estimated A*(ν)')

# Labels and title
ax.set_xlabel('Viscosity ν')
ax.set_ylabel('Initial Amplitude A₀')
ax.set_title('Phase Map of Regularity Detection (CFL = 1.0)')
ax.legend()
plt.colorbar(c, ticks=[0, 1], label='0: Regularity, 1: Failure')

# Save figure
output_path = "/mnt/data/ns_phase_map.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print("Phase map saved as:", output_path)
