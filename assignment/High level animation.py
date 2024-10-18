import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Read CSV files
data = pd.read_csv('latest_since_midnight_maxmin.csv')

# Calculate the temperature difference
data['Temperature Difference'] = data['Maximum Air Temperature Since Midnight(degree Celsius)'] - data['Minimum Air Temperature Since Midnight(degree Celsius)']

# Setting up the chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.set_xlim(-1, 1)
ax1.set_ylim(-1, 1)
ax1.set_xticks([])
ax1.set_yticks([])

# Add a circle
circle1 = plt.Circle((0, 0), 0.1, color='r')
ax1.add_patch(circle1)

# Animation parameters
max_loop = 100
full_circle_radius = 1
number_of_lines = 200
scale = 30
reverse = False

# Setting Temperature Difference Chart
x_bar = np.arange(len(data))
bars = ax2.bar(x_bar, [0]*len(data), color='purple', label='Temperature Difference')
ax2.set_ylim(0, data['Temperature Difference'].max() + 1)
ax2.set_title('Temperature Difference (Max - Min)')
ax2.set_xlabel('Index')
ax2.set_ylabel('Temperature Difference (°C)')
ax2.legend()

def update(frame):
    global reverse
    if frame % max_loop == 0:
        reverse = not reverse
    
    if reverse:
        frame = frame % max_loop
    else:
        frame = max_loop - frame % max_loop
    
    norm_frame = frame / max_loop
    
  # Update the circle
    circle1.set_radius(full_circle_radius * norm_frame)
    circle1.set_color(plt.cm.viridis(norm_frame))

  # Generate X-values
    x = np.linspace(-1, 1, int(norm_frame * max_loop))
    y = np.cos(x * frame / scale)
    z = np.sin(x * frame / scale)
    
    if reverse:
        y = -y
        z = -z

# Drawing curves in animation
    ax1.clear()
    ax1.set_xlim(-1, 1)
    ax1.set_ylim(-1, 1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    
    ax1.plot(x, y, color=plt.cm.viridis(norm_frame), alpha=0.5)
    ax1.plot(x, z, color=plt.cm.viridis(-norm_frame), alpha=0.5)

    # Update bar chart colors
    for i, bar in enumerate(bars):
        bar.set_height(data['Temperature Difference'][i] * (frame / len(data)))
        bar.set_color(plt.cm.viridis(i / len(bars))) # Use gradient colors

    # Remove excess lines
    while len(ax1.lines) > number_of_lines * norm_frame:
        ax1.lines[0].remove()

# Create animations
animation = FuncAnimation(fig, update, interval=10)
plt.show()
