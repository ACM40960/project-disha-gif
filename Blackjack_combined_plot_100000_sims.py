import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Import simulation functions from other modules
from Blackjack_Inexperienced_player import run_simulation_100000_times_inexperienced_blackjack
from Blackjack_simple_logic import run_simulation_100000_times_simple_blackjack
from Blackjack_with_splitting import simulate_100000_times_with_splitting

# Set the random seed for reproducibility
random.seed(5082)

# Function to plot the results of all three simulators
def plot_simulator_results(results1, results2, results3):
    labels = ['Inexperienced', 'Simple', 'Complex (with splitting)']
    total_simulations = 100000
    
    # Calculate win, loss, and tie percentages for each simulator
    win_percentages = [(results1['wins'] / total_simulations) * 100,
                       (results2['wins'] / total_simulations) * 100,
                       (results3['wins'] / total_simulations) * 100]

    loss_percentages = [(results1['losses'] / total_simulations) * 100,
                        (results2['losses'] / total_simulations) * 100,
                        (results3['losses'] / total_simulations) * 100]

    tie_percentages = [(results1['ties'] / total_simulations) * 100,
                       (results2['ties'] / total_simulations) * 100,
                       (results3['ties'] / total_simulations) * 100]
    
    # Set up the plot
    x = range(len(labels))
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_width = 0.2
    
    # Create the bar plot for win, loss, and tie percentages
    ax.bar(x, win_percentages, width=bar_width, label='Win', color='green')
    ax.bar([pos + bar_width for pos in x], loss_percentages, width=bar_width, label='Loss', color='red')
    ax.bar([pos + bar_width * 2 for pos in x], tie_percentages, width=bar_width, label='Tie/Push', color='gray')

    ax.set_xlabel('TYPE OF STRATEGY')
    ax.set_ylabel('Percentage')
    ax.set_title('Blackjack Simulation Results (100000 simulations)')
    ax.set_xticks([pos + bar_width for pos in x])
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.2f}%', xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3), textcoords='offset points', ha='center', va='bottom')
   
    # Function to add labels to the bars
    autolabel(ax.patches[:3])
    autolabel(ax.patches[3:6])
    autolabel(ax.patches[6:])

    plt.tight_layout()
    plt.show()

# Call the functions to get the simulation results
random.seed(5082) # set seed for reproducibility
sim_results_experienced_blackjack = simulate_100000_times_with_splitting()
sim_results_simple_blackjack = run_simulation_100000_times_simple_blackjack()
sim_results_inexperienced_blackjack = run_simulation_100000_times_inexperienced_blackjack()

# Plot the results of all three simulators
plot_simulator_results(sim_results_inexperienced_blackjack, sim_results_simple_blackjack, sim_results_experienced_blackjack)