import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = pd.read_csv('latest_since_midnight_maxmin.csv')

# Setting up charts
fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(data))  # Using indexes as data for the x-axis
lines, = ax.plot(x, data['Maximum Air Temperature Since Midnight(degree Celsius)'], 'r-', label='Max Temperature', marker='o')
lines2, = ax.plot(x, data['Minimum Air Temperature Since Midnight(degree Celsius)'], 'b-', label='Min Temperature', marker='x')
ax.set_xlim(0, len(data) - 1)
ax.set_ylim(data['Minimum Air Temperature Since Midnight(degree Celsius)'].min() - 1, data['Maximum Air Temperature Since Midnight(degree Celsius)'].max() + 1)
ax.set_title('Maximum and Minimum Air Temperature Since Midnight')
ax.set_xlabel('Index')
ax.set_ylabel('Temperature (degree Celsius)')
ax.legend()

# Initialization function: background of the graph
def init():
    lines.set_data([], [])
    lines2.set_data([], [])
    return lines, lines2

# Update function: called once per frame
def update(frame):
    # Ensure that the lengths of the x and y data match
    x_data = [i for i in range(frame+1)]
    y1_data = data['Maximum Air Temperature Since Midnight(degree Celsius)'][:frame+1]
    y2_data = data['Minimum Air Temperature Since Midnight(degree Celsius)'][:frame+1]
    lines.set_data(x_data, y1_data)
    lines2.set_data(x_data, y2_data)
    return lines, lines2

# Creating Animations
ani = FuncAnimation(fig, update, frames=len(data), init_func=init, blit=False)  # 将blit设置为False

plt.show()