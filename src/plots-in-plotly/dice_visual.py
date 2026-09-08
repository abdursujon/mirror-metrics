import plotly.express as px
from die import Die 

'''Handles two rolling dice to create a plot''' 

die_1 = Die()
die_2 = Die()

results = [(die_1.roll() + die_2.roll()) for _ in range(1000)]

# Analyse the results of dice roll 
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(value) for value in poss_results]

# Visualise the results (other fig funcitons: scatter, line, funnel, timeline)
title = "Result of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result: Die Numbers from 2 to 12', 'y': 'Frequency of Result'}

# Further customisation of chart each bar 
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels) 
fig.update_layout(xaxis_dtick=1)
fig.write_image('/home/sujon/Project/mirror-metrics/output/graph/rolling_two_dice_probability.png', width=1200, height=600)
fig.show()