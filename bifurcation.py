import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    """Compute one iteration of the logistic map with parameter r."""
    return r * x * (1 - x)

# Parameters
n_skip = 200  # Number of iterations to skip (transient)
n_iter = 100  # Number of iterations to plot
n_rs = 1000  # Number of r values to use
rs = np.linspace(2.5, 4.0, n_rs)  # Range of r values
xs = np.empty(n_iter)  # Array to store orbit

# For each r value, compute orbit and plot points
plt.figure(figsize=(10, 6))
for r in rs:
    x = 0.1  # Initial condition
    
    # Skip transient iterations
    for i in range(n_skip):
        x = logistic_map(r, x)
    
    # Compute orbit points to plot
    for i in range(n_iter):
        x = logistic_map(r, x)
        xs[i] = x
    
    # Plot points
    plt.plot([r] * n_iter, xs, 'k,', alpha=0.1)

plt.title("Bifurcation Diagram of the Logistic Map", fontsize=14)
plt.xlabel("Parameter (r)", fontsize=12)
plt.ylabel("State (x)", fontsize=12)
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig("bifurcation_diagram.png", dpi=300)
plt.show() 