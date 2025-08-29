import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points
Y, X = np.mgrid[-2:2:100j, -3:3:100j]

# Define the wing shape (simple airfoil)
wing_x = np.linspace(-1, 1, 100)
wing_y = 0.2 * np.sin(np.pi * wing_x)

# Define airflow: uniform flow + vortex for lift
U = 1.0  # uniform flow speed
V = 0.0

# Add circulation for lift
gamma = 2.0  # circulation strength
u = U - gamma * (Y / (X**2 + Y**2))
v = V + gamma * (X / (X**2 + Y**2))

# Plot streamlines
plt.figure(figsize=(8, 4))
plt.streamplot(X, Y, u, v, color='b', density=2)
plt.plot(wing_x, wing_y, color='k', linewidth=3)  # wing profile
plt.title("2D Airflow Over an Airplane Wing")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.grid(True)
plt.show()