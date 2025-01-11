import numpy as np
import matplotlib.pyplot as plt

# Logistic map parameters
r_values = np.linspace(2.5, 4.0, 10000)
iterations = 1000
last = 100

x = 1e-5 * np.ones_like(r_values)

# Prepare the plot
plt.figure(figsize=(10, 7))

for i in range(iterations):
    x = r_values * x * (1 - x)
    if i >= (iterations - last):
        plt.plot(r_values, x, ',k', alpha=0.1)

plt.title("Bifurcation Diagram of the Logistic Map", fontsize=16)
plt.xlabel("Growth Rate (r)")
plt.ylabel("Population")
plt.show()
