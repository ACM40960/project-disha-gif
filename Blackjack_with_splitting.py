# Blackjack simulator with splitting 

import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Set the random seed for reproducibility
random.seed(43209)

# Function to create a new deck of cards
def create_deck():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return deck * 4  # Four copies of each card to represent a single deck

# Function to shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Function to deal a card from the deck
def deal_card(deck):
    return deck.pop()

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            value += 11
            num_aces += 1
        else:
            value += int(card)

    # Adjust the value if there are aces and the hand value exceeds 21
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    # If there are still aces left and the value is greater than 21, convert the remaining aces to 1
    while num_aces > 0 and value > 21:
        value -= 10
        num_aces -= 1

    return value

# Function to simulate the game
def simulate_blackjack():
    # Create and shuffle the deck
    deck = create_deck()
    shuffle_deck(deck)

    # Deal initial cards
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Helper function to check if the player's hand can be split
    def can_split(hand):
        return len(hand) == 2 and hand[0] == hand[1]

    # Player's turn
    while True:
        player_value = calculate_hand_value(player_hand)
        dealer_upcard = dealer_hand[0]

        # Check for special cases: blackjack and soft hands
        if player_value == 21 and len(player_hand) == 2:
            return 'win' if calculate_hand_value(dealer_hand) != 21 else 'tie'
        if 'A' in player_hand and player_value == 11:
            player_hand[player_hand.index('A')] = 'A'  # Convert Ace from 11 to 1

        # Use basic strategy to determine the player's action
        if player_value >= 17:
            break
        elif player_value <= 11:
            player_hand.append(deal_card(deck))
        elif can_split(player_hand) and player_hand[0] in ['2', '3', '7', '8']:
            # Split if the hand contains a pair of 2s, 3s, 7s, or 8s
            player_hand_1 = [player_hand[0], deal_card(deck)]
            player_hand_2 = [player_hand[1], deal_card(deck)]

            # Simulate the first hand after splitting
            player_value_1 = simulate_hand_after_split(player_hand_1, deck, dealer_hand)

            # Simulate the second hand after splitting
            player_value_2 = simulate_hand_after_split(player_hand_2, deck, dealer_hand)

            # Compare the results of the two hands and return the best outcome
            if player_value_1 > 21 and player_value_2 > 21:
                return 'loss'
            elif player_value_1 > 21 or (player_value_2 <= 21 and player_value_2 > player_value_1):
                player_hand = player_hand_2
            else:
                player_hand = player_hand_1
        
        elif player_value == 12 and dealer_upcard in ['4', '5', '6']:
            break
        elif player_value >= 13 and player_value <= 16 and dealer_upcard in ['2', '3', '4', '5', '6']:
            break
        elif player_value == 9 and dealer_upcard in ['2', '3', '4', '5', '6']:
            player_hand.append(deal_card(deck))
        elif player_value == 10 and dealer_upcard not in ['10', 'A']:
            player_hand.append(deal_card(deck))
        elif player_value == 11 and dealer_upcard != 'A':
            player_hand.append(deal_card(deck))
        else:
            break

    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    # Compare hands and determine the winner
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        return 'win'
    elif player_value < dealer_value:
        return 'loss'
    else:
        return 'tie'

# Function to simulate the player's turn after splitting
def simulate_hand_after_split(hand, deck, dealer_hand):
    while True:
        hand_value = calculate_hand_value(hand)
        dealer_upcard = dealer_hand[0]

        if hand_value >= 17:
            break
        elif hand_value <= 11:
            hand.append(deal_card(deck))
        elif hand_value >= 13 and hand_value <= 16 and dealer_upcard in ['2', '3', '4', '5', '6']:
            break
        else:
            hand.append(deal_card(deck))

    return calculate_hand_value(hand)

# Function to perform simulations
def simulation(num_simulations):
    # Set seed for reproducibility
    random.seed(1010)
    global results ## Use the global results dictionary
    results = {'win': 0, 'loss': 0, 'tie': 0}

    for _ in range(num_simulations):
        outcome = simulate_blackjack()
        results[outcome] += 1

    win_percentage = results['win'] / num_simulations * 100
    loss_percentage = results['loss'] / num_simulations * 100
    tie_percentage = results['tie'] / num_simulations * 100

    print(f"Results after {num_simulations} simulations:")
    print(f"Win: {win_percentage}%")
    print(f"Loss: {loss_percentage}%")
    print(f"Tie: {tie_percentage}%")
    
    # Create a bar chart to visualize results
    labels = ['Win', 'Loss', 'Push']
    sizes = [results['win'], results['loss'], results['tie']]
    colors = ['green', 'red', 'gray']

    plt.bar(labels, sizes, color=colors)
    plt.title(f'Simulation (with splitting) Results ({num_simulations} simulations)')
    plt.ylabel('Number of Occurrences')
    for i, size in enumerate(sizes):
        plt.text(i, size + 2, f"{(size / num_simulations) * 100:.2f}%", ha='center')
    
    plt.show()

# Function to simulate 100000 times and store the results for final plot
def simulate_100000_times_with_splitting():
    num_simulations = 100000
    results = {'wins': 0, 'losses': 0, 'ties': 0}

    for _ in range(num_simulations):
        outcome = simulate_blackjack()
        if outcome == 'win':
            results['wins'] += 1
        elif outcome == 'loss':
            results['losses'] += 1
        else:
            results['ties'] += 1

    return results

# Function to be called when the "Run Simulation" button is clicked
def run_simulation():
    num_simulations_str = num_simulations_entry.get()
    
    if not num_simulations_str.isdigit():
        tk.messagebox.showerror("Invalid Input", "Please enter a valid integer.")
        return
    
    try:
        num_simulations = int(num_simulations_str)
        simulation(num_simulations)
    except ValueError:
        tk.messagebox.showerror("Invalid Input", "Please enter a valid integer.")

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
