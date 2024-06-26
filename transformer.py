import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Define the tear drop shape in polar coordinates
def teardrop(rho):
    theta = np.linspace(0, 2 * np.pi, 100)
    r = rho * (1 - np.cos(theta))
    return r, theta

# Transform the tear drop shape into an ellipsoid
def teardrop_to_ellipsoid(r, theta, a, b, c, rho):
    phi = (np.pi / 2) * (1 - r / rho)
    x = a * np.outer(np.sin(phi), np.cos(theta))
    y = b * np.outer(np.sin(phi), np.sin(theta))
    z = c * np.outer(np.cos(phi), np.ones_like(theta))
    return x, y, z

# Parameters for the shapes
rho = 1.0  # Radius of the tear drop
a, b, c = 1.0, 0.5, 0.5  # Ellipsoid axes

# Generate the tear drop shape
r, theta = teardrop(rho)

# Generate the ellipsoid shape from the tear drop
x_ellipsoid, y_ellipsoid, z_ellipsoid = teardrop_to_ellipsoid(r, theta, a, b, c, rho)

# Set up the figure and axis
fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot(121, projection='3d')

# Initial plot for the tear drop shape
x_teardrop = r * np.cos(theta)
y_teardrop = r * np.sin(theta)
z_teardrop = np.zeros_like(r)
teardrop_plot, = ax.plot(x_teardrop, y_teardrop, z_teardrop, label='Tear Drop Shape')
ax.set_title('Tear Drop to Ellipsoid Transformation')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Function to update the frame
def update(frame):
    t = frame / num_frames
    x = (1 - t) * x_teardrop + t * x_ellipsoid
    y = (1 - t) * y_teardrop + t * y_ellipsoid
    z = (1 - t) * z_teardrop + t * z_ellipsoid
    ax.clear()
    ax.plot_surface(x, y, z, color='b', alpha=0.7)
    ax.set_title('Tear Drop to Ellipsoid Transformation')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

# Number of frames for the animation
num_frames = 100

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50)

plt.show()
