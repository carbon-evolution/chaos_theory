import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def mandelbrot(h, w, max_iter, x_min=-2.5, x_max=1.0, y_min=-1.25, y_max=1.25):
    """Generate the Mandelbrot set."""
    y, x = np.ogrid[y_min:y_max:h*1j, x_min:x_max:w*1j]
    c = x + y*1j
    z = c.copy()
    
    # Initialize the output array
    mandelbrot_set = np.zeros((h, w), dtype=int)
    
    # For each pixel, check if the sequence diverges
    for i in range(max_iter):
        mask = np.abs(z) < 2.0
        mandelbrot_set[mask] = i
        z[mask] = z[mask]**2 + c[mask]
    
    return mandelbrot_set

# Parameters
h, w = 1000, 1500  # Height and width of the output image
max_iter = 100  # Maximum number of iterations

# Generate the Mandelbrot set
mandelbrot_set = mandelbrot(h, w, max_iter)

# Create a custom colormap
colors = [(0, 0, 0), (0, 0, 0.5), (0, 0, 1), (0, 0.5, 1), 
          (0, 1, 1), (0.5, 1, 0.5), (1, 1, 0), (1, 0.5, 0), (1, 0, 0)]
colormap = LinearSegmentedColormap.from_list("mandelbrot", colors, N=max_iter)

# Display the result
plt.figure(figsize=(15, 10))
plt.imshow(mandelbrot_set, cmap=colormap)
plt.axis('off')
plt.title("Mandelbrot Set", fontsize=14)
plt.tight_layout()
plt.savefig("mandelbrot.png", dpi=300, bbox_inches='tight')
plt.show()

# Function to zoom into a specific region of the Mandelbrot set
def zoom_mandelbrot(center_x, center_y, zoom_width, zoom_height):
    """Create a zoomed view of the Mandelbrot set at the specified coordinates."""
    x_min = center_x - zoom_width/2
    x_max = center_x + zoom_width/2
    y_min = center_y - zoom_height/2
    y_max = center_y + zoom_height/2
    
    h, w = 1000, 1000
    max_iter = 200  # Increase iterations for zoom
    
    zoomed_set = mandelbrot(h, w, max_iter, x_min, x_max, y_min, y_max)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(zoomed_set, cmap=colormap)
    plt.axis('off')
    plt.title(f"Mandelbrot Zoom (center: {center_x:.3f}, {center_y:.3f}, width: {zoom_width:.3f})", fontsize=14)
    plt.tight_layout()
    plt.savefig(f"mandelbrot_zoom_{center_x:.3f}_{center_y:.3f}.png", dpi=300, bbox_inches='tight')
    plt.show()

# Example zoom locations (interesting regions of the Mandelbrot set)
# Uncomment to generate zoomed views
# zoom_mandelbrot(-0.75, 0.1, 0.1, 0.1)  # Near the main bulb
# zoom_mandelbrot(-0.1, 0.8, 0.05, 0.05)  # In the upper feathers
# zoom_mandelbrot(-1.75, 0.0, 0.05, 0.05)  # Left side detail 