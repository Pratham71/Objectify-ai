import numpy as np
import matplotlib.pyplot as plt

# Defining sections of the piecewise vase function
def vase_func(x):
    if 0 <= x <= 8:
        return 0.0459 * x**2 - 1.13 * x + 10.3 
    elif 8 < x <= 16.4:
        return 0.05 * (16.4 - x)**2  
    else:
        return 0  # Outside bounds

x_vals = np.linspace(0, 16.4, 500)
theta_vals = np.linspace(0, 2 * np.pi, 200)
x_vals, theta_vals = np.meshgrid(x_vals, theta_vals)

r_vals = np.vectorize(vase_func)(x_vals)
y_vals = r_vals * np.cos(theta_vals)
z_vals = r_vals * np.sin(theta_vals)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_vals, y_vals, z_vals, cmap='viridis', alpha=0.8)

ax.set_xlabel('X-axis (Height)')
ax.set_ylabel('Y-axis (Radius)')
ax.set_zlabel('Z-axis (Radius)')
plt.title("3D Model of Vase Surface of Revolution")
plt.show()
