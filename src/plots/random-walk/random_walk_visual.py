import matplotlib.pyplot as plt 
from random_walk import RandomWalk

plt.style.use('classic')

while True:
    # Make a random walk 
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk 
    fig, ax = plt.subplots(figsize=(15, 9)) # subplots create figure and axes(subplot) at the same time 
    point_numbers = range(rw.num_points)

    # c = different colors for each point based on a sequence
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    #emphasize the first and last points 
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # remove the axes with numbers 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_aspect('equal')
    ax.set_title("Random Walk", fontsize=28)
    ax.set_xlabel("X Value", fontsize=18)
    ax.set_ylabel("Y Value", fontsize=18)

    plt.savefig('/home/sujon/Project/mirror-metrics/output/graph/random_walk', bbox_inches='tight', dpi=128)

    # Keep making new random walks as long as the program is active 
    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
    plt.close()

plt.show()