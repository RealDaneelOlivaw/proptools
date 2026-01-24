"""Plot expansion ratio vs chamber pressure."""
import numpy as np
import matplotlib.pyplot as plt
from proptools import nozzle

# Fixed parameters
p_e = 100e3    # Exit pressure [units: pascal]
gamma = 1.4    # Exhaust heat capacity ratio [units: dimensionless]

# Chamber pressure range [units: pascal]
p_c_range = np.linspace(1e6, 10e6, 100)

# Calculate expansion ratio for each chamber pressure
exp_ratios = []
for p_c in p_c_range:
    exp_ratio = nozzle.er_from_p(p_c, p_e, gamma)
    exp_ratios.append(exp_ratio)

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(p_c_range / 1e6, exp_ratios, 'b-', linewidth=2)
plt.xlabel('Chamber Pressure [MPa]')
plt.ylabel('Expansion Ratio [-]')
plt.title('Expansion Ratio vs Chamber Pressure')
plt.grid(True, alpha=0.3)
plt.show()
