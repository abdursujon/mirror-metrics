import matplotlib.pyplot as plt
import math

'''
This is an expriment which creats a wave of form to create an art. 
The art png is avaiable int he directory: output/art/art_one.png
'''
x_values = [i * 0.1 for i in range(499)]
x_values = list(range(5000))
y_values = [100 * math.sin(x) for x in x_values]

fig, ax = plt.subplots(figsize=(10, 6)) 

ax.plot(x_values, y_values, color='red', linewidth=1, zorder=1)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=20, zorder=2)
ax.set_title("Wave Pattern", fontsize=28)
ax.set_xlabel("Value", fontsize=18)
ax.set_ylabel("Amplitude", fontsize=18)

plt.savefig('/home/sujon/Project/mirror-metrics/output/art/art_one.png', bbox_inches='tight', dpi=100)
plt.show()