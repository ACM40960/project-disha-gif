# Blackjack simple logic 
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Function to simulate a single blackjack game with simple logic (no splitting)
def play_blackjack():
    # Create a deck of cards with four copies of each value
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(deck)
    
    # Deal initial hands for the player and dealer
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    # Function to calculate the value of a hand, considering Aces as 1 or 11
    def get_hand_value(hand):
        value = sum(hand)
        if value > 21 and 11 in hand:
            hand.remove(11)
            hand.append(1)
            value = get_hand_value(hand)
        return value
    
    # Function to add a card to a hand
    def hit(hand):
        hand.append(deck.pop())

    # Player's turn: Keep hitting until the hand value is at least 17
    while get_hand_value(player_hand) < 17:
        hit(player_hand)
        if get_hand_value(player_hand) > 21:
            return -1  # Player busts, return -1 (loss)
        
    # Dealer's turn: Keep hitting until the hand value is at least 17
    while get_hand_value(dealer_hand) < 17:
        hit(dealer_hand)
        if get_hand_value(dealer_hand) > 21:
            return 1  # Dealer busts, return 1 (win)

    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)

    if player_value == dealer_value:
        return 0  # Push, return 0
    elif player_value > dealer_value:
        return 1  # Player wins, return 1
    else:
        return -1  # Dealer wins, return -1

# Function to simulate blackjack for a given number of times and print the results
def simulate_simple_blackjack(num_simulations):
    # Set seed for reproducibility
    random.seed(213020)
    wins = 0
    losses = 0
    pushes = 0

    for _ in range(num_simulations):
        result = play_blackjack()
        if result == 1:
            wins += 1
        elif result == -1:
            losses += 1
        else:
            pushes += 1

    total_games = wins + losses + pushes
    win_percentage = (wins / total_games) * 100
    loss_percentage = (losses / total_games) * 100
    push_percentage = (pushes / total_games) * 100
    
    # Display simulation results
    print(f"Total games played: {total_games}")
    print(f"Win percentage: {win_percentage:.2f}%")
    print(f"Loss percentage: {loss_percentage:.2f}%")
    print(f"Push percentage: {push_percentage:.2f}%")
    
    labels = ['Win', 'Loss', 'Push']
    sizes = [wins, losses, pushes]
    colors = ['green', 'red', 'gray']
    
    # Create a bar chart to visualize the simulation results
    plt.bar(labels, sizes, color=colors)
    plt.title(f'Simplified Blackjack Simulation Results ({num_simulations} simulations)')
    plt.ylabel('Number of Occurrences')
    for i, size in enumerate(sizes):
        plt.text(i, size + 2, f"{(size / total_games) * 100:.2f}%", ha='center')
    
    plt.show()
    plt.show()
    
# Function to be called when the "Run Simulation" button is clicked
def run_simulation():
    num_simulations_str = num_simulations_entry.get()
    
    if not num_simulations_str.isdigit():
        tk.messagebox.showerror("Invalid Input", "Please enter a valid integer.")
        return
    
    num_simulations = int(num_simulations_str)
    simulate_simple_blackjack(num_simulations)

# Run the simulation 100000 times and store the result for the combined plot
def run_simulation_100000_times_simple_blackjack():
    num_simulations = 100000
    results = {'wins': 0, 'losses': 0, 'ties': 0}

    for _ in range(num_simulations):
        result = play_blackjack()
        if result == 1:
            results['wins'] += 1
        elif result == -1:
            results['losses'] += 1
        else:
            results['ties'] += 1

    return results

# ----------------------- GUI ------------------------------    
# Create the main window for the GUI
root = tk.Tk()
root.title("Blackjack Simulator")

# Create GUI components
num_simulations_label = tk.Label(root, text="Number of Simulations:")
num_simulations_entry = ttk.Entry(root)
run_button = ttk.Button(root, text="Run Simulation", command=run_simulation)

# Layout GUI components
num_simulations_label.pack()
num_simulations_entry.pack()
run_button.pack()

# Start the GUI event loop
root.mainloop()
