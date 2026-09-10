from pathlib import Path 
import csv 
import matplotlib.pyplot as plt 

path = Path('../../data/csv_files/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# I need position 2, 7, 8

# Extract hight temp 
highs = []
for row in reader: 
    if row[7]:
        high = float(row[7])
        highs.append(high)

# Plot hight temp 
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
ax.plot(highs, color='red')
ax.set_title("Sitka Daily High Temperature, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
plt.show()