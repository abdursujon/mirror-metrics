# pyplot: a visuatlisation package in matplotlib. here we import pyplot with alias plt so we don't have to repeatedly use the word pyplot 
import matplotlib.pyplot as plt 

'''
Line graph visualisation of square numbers. 
subplot() function can generate one or more plots in the same figure 
fig variable: represents the entire figure 
ax variable: the plot area where the data is drawn 
plt.show(): opens matplotlib viewer and displays the plot 
'''
print(plt.style.available)
x_values = range(1, 30)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots(figsize=(10, 6)) # width and height in inches 


# ploting the line 
ax.plot(x_values, y_values, color='red', linewidth=2, zorder=1)

# styling indivual points, s is the size of the points 
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greys, s=50, zorder=2) # RGB color=(0,0.8,0)

# set chart title and label axes 
ax.set_title("Square Numbers Line Graph", fontsize=28)
ax.set_xlabel("Value", fontsize=18)
ax.set_ylabel("Square of Value", fontsize=18)

#set size of tick labels (axis numbers)
ax.tick_params(labelsize=14)

# ticklabel_format() method allows us to override the default tick label style for any plot.
ax.ticklabel_format(style='plain') # other style: sci(scietific), engineering(1e+3 etc)

#set the range for the each axis 
ax.axis([0, 30, 0, 1000])

# we can save the figure through code in a directory (dpi = dots per inch allows us to install better quality picture)
# bbox_inches: Removes extra whitespace around the figure when saving:
plt.savefig('/home/sujon/Project/mirror-metrics/output/graph/line_square_graph.png', bbox_inches='tight', dpi=100)
plt.show()

