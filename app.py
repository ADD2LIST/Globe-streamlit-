import streamlit as st

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def rotate_globe(theta, phi):

    """Rotates the globe around the x-axis by theta degrees and around the y-axis by phi degrees.

    Args:

        theta: The angle of rotation around the x-axis in degrees.

        phi: The angle of rotation around the y-axis in degrees.

    Returns:

        The rotated globe.

    """

    # Create a 3D axes object.

    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    # Create a grid of points on the globe.

    theta_range = np.linspace(0, 360, 100)

    phi_range = np.linspace(-90, 90, 100)

    x, y, z = np.meshgrid(theta_range, phi_range, copy=False)

    # Rotate the grid of points.

    x = x * np.cos(theta) - y * np.sin(theta)

    y = x * np.sin(theta) + y * np.cos(theta)

    # Plot the rotated grid of points.

    ax.plot_surface(x, y, z, cmap='cool', alpha=0.5)

    # Set the title of the plot.

    ax.set_title('Rotating Globe')

    # Show the plot.

    plt.show()

# Create a Streamlit app.

app = st.py_app()

# Add a slider to control the rotation of the globe around the x-axis.

theta = st.slider('Rotation angle around x-axis (degrees)', 0, 360)

# Add a slider to control the rotation of the globe around the y-axis.

phi = st.slider('Rotation angle around y-axis (degrees)', 0, 360)

# Call the `rotate_globe` function to rotate the globe.

rotate_globe(theta, phi)


        





