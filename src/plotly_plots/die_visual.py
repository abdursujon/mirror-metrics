import plotly.express as px
from die import Die 

die = Die()
results = []
for number_of_roll in range(1000):
    result = die.roll()
    results.append(result)

# Analyse the results of dice roll 
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results (other fig funcitons: scatter, line, funnel, timeline)
title = "Frequency of Each Number of A Rolling Die 1000 Times"
labels = {'x': 'Die Numbers from 1 to 6', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels) 
fig.show()