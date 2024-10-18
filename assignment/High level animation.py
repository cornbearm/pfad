import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.transforms as transforms

# Read CSV files
data = pd.read_csv('latest_since_midnight_maxmin.csv')

# Setting up the chart
fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(data))  # Use the index as the x-axis of the data
lines, = ax.plot(x, data['Maximum Air Temperature Since Midnight(degree Celsius)'], 'r-', label='Max Temperature', marker='o')
lines2, = ax.plot(x, data['Minimum Air Temperature Since Midnight(degree Celsius)'], 'b-', label='Min Temperature', marker='x')
ax.set_xlim(0, len(data) - 1)
ax.set_ylim(data['Minimum Air Temperature Since Midnight(degree Celsius)'].min() - 1, data['Maximum Air Temperature Since Midnight(degree Celsius)'].max() + 1)
ax.set_title('Maximum and Minimum Air Temperature Since Midnight')
ax.set_xlabel('Index')
ax.set_ylabel('Temperature (degree Celsius)')
ax.legend()

# Add a subgraph for dynamic shapes
fig2, ax2 = plt.subplots(figsize=(3, 3), facecolor='white', frameon=False)
ax2.set_xlim(-1, 1), ax2.set_xticks([])
ax2.set_ylim(-1, 1), ax2.set_yticks([])

circle1 = plt.Circle((0, 0), 0.1, color='r')
ax2.add_patch(circle1)
square = [[-0.5, -0.5], [-0.5, 0.5], [0.5, 0.5], [0.5, -0.5]]
trans = (transforms.Affine2D().rotate_deg(45) + ax2.transData)
square = plt.Polygon(square, fill=None, transform=trans)
ax2.add_patch(square)

max_loop = 100
full_circle_radius = 1

reverse = False

# Initialization functions: background for charts
def init():
    lines.set_data([], [])
    lines2.set_data([], [])
    return lines, lines2

# Update function: called once per frame
def update(frame):
    global reverse
    x_data = [i for i in range(frame+1)]
    y1_data = data['Maximum Air Temperature Since Midnight(degree Celsius)'][:frame+1]
    y2_data = data['Minimum Air Temperature Since Midnight(degree Celsius)'][:frame+1]
    lines.set_data(x_data, y1_data)
    lines2.set_data(x_data, y2_data)

    if frame % max_loop == 0:
        reverse = not reverse
    if reverse:
        frame = frame % max_loop
    else:
        frame = max_loop - frame % max_loop

    norm_frame = frame/max_loop
    circle1.set_radius(full_circle_radius*norm_frame)
    circle1.set_color(plt.cm.viridis(norm_frame))
    transform = transforms.Affine2D().rotate_deg(90*norm_frame) + ax2.transData
    square.set_transform(transform)
    
    return lines, lines2, circle1, square

# Create animations
ani = FuncAnimation(fig, update, frames=len(data), init_func=init, blit=True, interval=50)

plt.show()