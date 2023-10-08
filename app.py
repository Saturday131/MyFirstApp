import streamlit as st

st.write('Hello world!')

import random
import plotly.graph_objs as go
import statistics

def monte_carlo_dice_simulation(num_rolls):
    outcomes = [0, 0, 0, 0, 0, 0]  # Initialize counters for each dice face
    
    for _ in range(num_rolls):
        # Roll a fair six-sided dice (generate a random number from 1 to 6)
        result = random.randint(1, 6)
        outcomes[result - 1] += 1  # Increment the counter for the corresponding outcome
    
    return outcomes

# Number of dice rolls in the simulation
num_rolls = 10000

# Run the Monte Carlo simulation
dice_outcomes = monte_carlo_dice_simulation(num_rolls)

# Calculate basic statistics
mean_value = statistics.mean(dice_outcomes)
median_value = statistics.median(dice_outcomes)
std_deviation = statistics.stdev(dice_outcomes)

# Create a bar chart to visualize the outcomes
dice_faces = [1, 2, 3, 4, 5, 6]
trace = go.Bar(x=dice_faces, y=dice_outcomes, text=dice_outcomes, textposition='auto', name='Dice Rolls')

# Create a text box to display statistics on the plot
statistics_text = f"Mean: {mean_value:.2f}<br>Median: {median_value}<br>Std Deviation: {std_deviation:.2f}"
text_trace = go.Scatter(x=[4], y=[max(dice_outcomes) - 100], mode='text', text=[statistics_text], name='Statistics')

# Create the layout
layout = go.Layout(
    title=f"Monte Carlo Simulation for Dice Roll (Number of Rolls: {num_rolls})",
    xaxis=dict(title='Dice Face'),
    yaxis=dict(title='Frequency'),
)

# Create the figure and add the traces
fig = go.Figure(data=[trace, text_trace], layout=layout)

# Show the plot
fig.show()
