import pandas as pd
import matplotlib.pyplot as plt

# Ensure that the file path is correct
file_path = 'latest_since_midnight_maxmin.csv'

data = pd.read_csv(file_path)

# Plotting the maximum temperature for each weather station
plt.figure(figsize=(10, 6))
plt.plot(data['Automatic Weather Station'], data['Maximum Air Temperature Since Midnight(degree Celsius)'], label='Max Temperature', marker='o')

# Plotting the minimum temperature for each weather station
plt.plot(data['Automatic Weather Station'], data['Minimum Air Temperature Since Midnight(degree Celsius)'], label='Min Temperature', marker='x')

plt.title('Maximum and Minimum Air Temperature Since Midnight')
plt.xlabel('Automatic Weather Station')
plt.ylabel('Temperature (degree Celsius)')
plt.xticks(rotation=90)  # Rotate the x-axis labels for better display
plt.legend()
plt.tight_layout()  # Automatically adjusts sub-map parameters to fill the entire image area
plt.show() 