import plotly.express as px
from die import Die 

die = Die()
results = [die.roll() for _ in range(1000)] # we can use _ when we don't need any loop variable 

# Analyse the results of dice roll
poss_results = range(1, die.num_sides+1)
frequencies =[results.count(value) for value in poss_results]

# Visualise the results (other fig funcitons: scatter, line, funnel, timeline)
title = "Frequency of Each Number of A Rolling Die 1000 Times"
labels = {'x': 'Die Numbers from 1 to 6', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels) 
fig.write_image('/home/sujon/Project/mirror-metrics/output/graph/rolling_one_dice_probability.png', width=1200, height=600)
fig.show()