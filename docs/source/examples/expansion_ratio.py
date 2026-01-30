"""Plot expansion ratio vs chamber pressure."""
import numpy as np
import matplotlib.pyplot as plt
from proptools import nozzle

# Fixed parameters
p_e = 100e3    # Exit pressure [units: pascal]
gamma = 1.4    # Exhaust heat capacity ratio [units: dimensionless]

# Chamber pressure range [units: pascal]
p_c_range = np.linspace(2e6, 6e6, 100)

# Calculate expansion ratio for each chamber pressure
exp_ratios = []
for p_c in p_c_range:
    exp_ratio = nozzle.er_from_p(p_c, p_e, gamma)
    exp_ratios.append(exp_ratio)

# Plot the results
plt.figure(figsize=(12/2.54, 9/2.54), dpi=300)
plt.plot(p_c_range / 1e6, exp_ratios, 'b-', linewidth=2)
plt.xlabel('Inet Pressure [MPa]', fontsize=12)
plt.ylabel('Ideal Expansion Ratio', fontsize=12)
plt.title('Ideal Expansion Ratio vs Inet Pressure', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tick_params(axis='both', which='major', labelsize=12, width=1.5, direction='in')
plt.gca().spines['bottom'].set_linewidth(1.5)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['top'].set_linewidth(1.5)
plt.gca().spines['right'].set_linewidth(1.5)
plt.tight_layout()
plt.savefig('expansion_ratio.png', dpi=300, bbox_inches='tight')
plt.show()
