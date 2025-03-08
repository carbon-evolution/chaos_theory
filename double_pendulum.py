import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Physical constants
G = 9.8  # Acceleration due to gravity (m/s^2)
L1, L2 = 1.0, 1.0  # Lengths of pendulum rods (m)
M1, M2 = 1.0, 1.0  # Masses of pendulum bobs (kg)

def derivatives(t, state):
    """Compute the derivatives of the double pendulum system."""
    theta1, omega1, theta2, omega2 = state
    
    # Equations of motion
    delta = theta2 - theta1
    den = (M1 + M2) * L1 - M2 * L1 * np.cos(delta) * np.cos(delta)
    
    # Angular acceleration for the first pendulum
    dtheta1 = omega1
    domega1 = (M2 * L1 * omega1 * omega1 * np.sin(delta) * np.cos(delta)
               + M2 * G * np.sin(theta2) * np.cos(delta)
               + M2 * L2 * omega2 * omega2 * np.sin(delta)
               - (M1 + M2) * G * np.sin(theta1)) / den
    
    # Angular acceleration for the second pendulum
    dtheta2 = omega2
    domega2 = (-M2 * L2 * omega2 * omega2 * np.sin(delta) * np.cos(delta)
               + (M1 + M2) * G * np.sin(theta1) * np.cos(delta)
               - (M1 + M2) * L1 * omega1 * omega1 * np.sin(delta)
               - (M1 + M2) * G * np.sin(theta2)) / (M2 * L2 - M2 * L2 * np.cos(delta) * np.cos(delta))
    
    return [dtheta1, domega1, dtheta2, domega2]

# Initial conditions (angles in radians, angular velocities in rad/s)
initial_state = [np.pi/2, 0, np.pi/2, 0]  # [theta1, omega1, theta2, omega2]

# Time span for the simulation
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the differential equations
solution = solve_ivp(derivatives, t_span, initial_state, t_eval=t_eval, method='RK45')

# Extract solution
theta1, omega1, theta2, omega2 = solution.y
times = solution.t

# Convert to Cartesian coordinates for visualization
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# Path tracing
path_length = 100  # Number of points to show in the path

# Plotting
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')
ax.grid()

# Plot elements
line, = ax.plot([], [], 'o-', lw=2)
path, = ax.plot([], [], '-', lw=1, alpha=0.5)

# Initialization function for animation
def init():
    line.set_data([], [])
    path.set_data([], [])
    return line, path

# Animation function
def animate(i):
    # Update pendulum position
    line.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    
    # Update path
    start_idx = max(0, i - path_length)
    path.set_data(x2[start_idx:i], y2[start_idx:i])
    
    return line, path

# Create animation
ani = FuncAnimation(fig, animate, frames=len(times),
                    init_func=init, blit=True, interval=20)

plt.title("Double Pendulum", fontsize=14)
plt.tight_layout()

# Uncomment to save the animation
# ani.save('double_pendulum.gif', writer='pillow', fps=30)

plt.show() 