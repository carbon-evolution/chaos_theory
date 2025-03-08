# Chaos Theory - Python Simulations and Visualizations

This repository contains a collection of Python programs exploring chaos theory and related mathematical concepts through simulations and visualizations.

## What is Chaos Theory?

Chaos theory is a branch of mathematics that studies the behavior of dynamical systems that are highly sensitive to initial conditions. This sensitivity, popularly referred to as the "butterfly effect," means that small differences in initial conditions can yield widely diverging outcomes, making long-term prediction impossible in general.

Key characteristics of chaotic systems include:
- **Sensitivity to initial conditions**: Tiny changes can lead to dramatically different results
- **Deterministic yet unpredictable**: Systems follow deterministic rules but can't be predicted in the long term
- **Nonlinearity**: Outputs are not directly proportional to inputs
- **Fractal properties**: Self-similar patterns that repeat at different scales

## Programs in this Repository

### 1. Lorenz Attractor (`chaos_theory.py`)
The Lorenz attractor is one of the most famous examples of a chaotic system, first studied by Edward Lorenz in 1963 while modeling atmospheric convection.

- Implements the Lorenz system of differential equations
- Visualizes the characteristic butterfly-shaped attractor in 3D
- Demonstrates sensitivity to initial conditions

### 2. Mandelbrot Set (`mandelbrot.py`)
The Mandelbrot set is one of the most famous fractals in mathematics, exhibiting infinite complexity.

- Generates high-resolution visualizations of the Mandelbrot set
- Uses customizable color maps for aesthetic rendering
- Includes functionality to zoom into specific regions of interest

### 3. Julia Sets (`julia_set.py`)
Julia sets are fractals related to the Mandelbrot set, generated from complex functions.

- Creates beautiful Julia set visualizations for a given complex parameter
- Customizable resolution and color mapping
- Includes optional animation functionality to demonstrate how Julia sets change with varying parameters

### 4. Hénon Map (`henon_map.py`)
The Hénon map is a discrete-time dynamical system that exhibits chaotic behavior.

- Generates the classic Hénon strange attractor
- Provides parameters to adjust the system behavior
- Includes optional functionality to visualize basins of attraction

### 5. Bifurcation Diagram (`bifurcation.py`)
Bifurcation diagrams show how a system's behavior changes as a parameter is varied, revealing the route to chaos.

- Visualizes the famous bifurcation diagram of the logistic map
- Demonstrates period-doubling and the transition to chaos
- Shows the universal Feigenbaum constant in action

### 6. Double Pendulum (`double_pendulum.py`)
The double pendulum is a simple physical system that exhibits chaotic motion.

- Simulates the motion of a double pendulum using differential equations
- Visualizes the system with an optional animation
- Demonstrates how a simple mechanical system can produce complex, unpredictable behavior

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries (install via pip):
  ```
  pip install -r requirements.txt
  ```

### Running the Simulations
Each program can be run independently:

```bash
python chaos_theory.py     # Lorenz attractor
python mandelbrot.py       # Mandelbrot set
python julia_set.py        # Julia set
python henon_map.py        # Hénon map
python bifurcation.py      # Bifurcation diagram
python double_pendulum.py  # Double pendulum simulation
```

## Output Examples

The repository includes several pre-generated visualization images:
- `mandelbrot.png` - The Mandelbrot set fractal
- `julia_set.png` - A Julia set fractal
- `henon_attractor.png` - The Hénon strange attractor
- `bifurcation_diagram.png` - Bifurcation diagram of the logistic map

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

These simulations are based on classical mathematical models in chaos theory and nonlinear dynamics. 