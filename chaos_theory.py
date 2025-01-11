import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorenz system parameters
sigma = 10
rho = 28
beta = 8/3

def lorenz(x, y, z, sigma, rho, beta):
    """Compute the derivatives for the Lorenz system."""
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

# Time step parameters
dt = 0.01  # Time step
num_steps = 10000  # Number of steps

# Initial conditions
x, y, z = 1.0, 1.0, 1.0  # Initial values of x, y, z

# Arrays to store the trajectory
xs = np.empty(num_steps)
ys = np.empty(num_steps)
zs = np.empty(num_steps)

xs[0], ys[0], zs[0] = x, y, z

# Perform the integration
for i in range(1, num_steps):
    dx, dy, dz = lorenz(x, y, z, sigma, rho, beta)
    x += dx * dt
    y += dy * dt
    z += dz * dt
    xs[i], ys[i], zs[i] = x, y, z

# Plot the 3D graph
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, lw=0.5, color='blue')
ax.set_title("Lorenz Attractor", fontsize=16)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
plt.show()
