import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def julia_set(h, w, c, max_iter):
    """Generate a Julia set for complex parameter c."""
    y, x = np.ogrid[-1.5:1.5:h*1j, -1.5:1.5:w*1j]
    z = x + y*1j
    
    # Initialize the output array
    julia = np.zeros((h, w), dtype=int)
    
    # For each pixel, check if the sequence diverges
    for i in range(max_iter):
        mask = np.abs(z) < 10
        julia[mask] = i
        z[mask] = z[mask]**2 + c
    
    return julia

# Parameters
h, w = 1000, 1000  # Height and width of the output image
max_iter = 100  # Maximum number of iterations
c = -0.7 + 0.27j  # Complex parameter for the Julia set

# Generate the Julia set
julia = julia_set(h, w, c, max_iter)

# Create a custom colormap
colors = [(0, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 0), (1, 0, 0)]
colormap = LinearSegmentedColormap.from_list("julia", colors, N=max_iter)

# Display the result
plt.figure(figsize=(10, 10))
plt.imshow(julia, cmap=colormap)
plt.axis('off')
plt.title(f"Julia Set (c = {c.real:.2f} + {c.imag:.2f}i)", fontsize=14)
plt.tight_layout()
plt.savefig("julia_set.png", dpi=300, bbox_inches='tight')
plt.show()

# Function to create animated Julia sets
def create_julia_animation():
    """Create a series of Julia set images by varying the parameter c."""
    # Range of parameters
    num_frames = 20
    real_range = np.linspace(-1.0, 0.5, num_frames)
    imag_range = np.linspace(-0.5, 0.5, num_frames)
    
    h, w = 500, 500  # Smaller size for animation
    max_iter = 100
    
    # Generate each frame
    for idx, (real, imag) in enumerate(zip(real_range, imag_range)):
        c = complex(real, imag)
        julia = julia_set(h, w, c, max_iter)
        
        plt.figure(figsize=(5, 5))
        plt.imshow(julia, cmap=colormap)
        plt.axis('off')
        plt.title(f"Julia Set (c = {c.real:.2f} + {c.imag:.2f}i)", fontsize=12)
        plt.tight_layout()
        plt.savefig(f"julia_frame_{idx:03d}.png", dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"Generated frame {idx+1}/{num_frames}")
    
    print("Animation frames complete. Use these images to create a GIF or video.")

# Uncomment to generate animation frames (creates multiple files)
# create_julia_animation() 