import numpy as np
import matplotlib.pyplot as plt

def henon_map(x, y, a=1.4, b=0.3):
    """Compute one iteration of the Hénon map."""
    x_next = 1 - a * x**2 + y
    y_next = b * x
    return x_next, y_next

# Parameters
num_points = 100000  # Number of points to generate
a = 1.4  # Traditional Hénon map parameter
b = 0.3  # Traditional Hénon map parameter
transient = 1000  # Number of iterations to skip (transient)

# Starting point
x, y = 0, 0

# Skip transient
for _ in range(transient):
    x, y = henon_map(x, y, a, b)

# Generate points for the attractor
points = np.zeros((num_points, 2))
for i in range(num_points):
    x, y = henon_map(x, y, a, b)
    points[i] = [x, y]

# Plot the attractor
plt.figure(figsize=(10, 8))
plt.scatter(points[:, 0], points[:, 1], s=0.1, color='blue')
plt.title(f"Hénon Map Attractor (a={a}, b={b})", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.axis('equal')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("henon_attractor.png", dpi=300)
plt.show()

# Function to visualize the basins of attraction
def plot_basins_of_attraction(a=1.4, b=0.3, resolution=500, max_iterations=100, escape_radius=10):
    """Plot the basins of attraction for the Hénon map."""
    x_min, x_max = -2.0, 2.0
    y_min, y_max = -2.0, 2.0
    
    x = np.linspace(x_min, x_max, resolution)
    y = np.linspace(y_min, y_max, resolution)
    X, Y = np.meshgrid(x, y)
    
    # Initialize array to store the number of iterations before escape
    iterations = np.zeros((resolution, resolution))
    
    # For each initial point, count iterations until escape
    for i in range(resolution):
        for j in range(resolution):
            x_init, y_init = X[i, j], Y[i, j]
            for k in range(max_iterations):
                x_init, y_init = henon_map(x_init, y_init, a, b)
                if x_init**2 + y_init**2 > escape_radius**2:
                    iterations[i, j] = k
                    break
            if iterations[i, j] == 0:  # If we didn't break, the point is considered in the set
                iterations[i, j] = max_iterations
    
    plt.figure(figsize=(10, 8))
    plt.imshow(iterations, cmap='viridis', extent=[x_min, x_max, y_min, y_max], origin='lower')
    plt.colorbar(label='Iterations before escape')
    plt.title(f"Basins of Attraction: Hénon Map (a={a}, b={b})", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.tight_layout()
    plt.savefig("henon_basins.png", dpi=300)
    plt.show()

# Uncomment to visualize basins of attraction (computationally intensive)
# plot_basins_of_attraction() 