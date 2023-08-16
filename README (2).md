# SIMULATE SINGLE DECK BLACKJACK
The Blackjack Simulation project offers a collection of Python scripts designed to allow users to simulate and analyze various aspects of the classic card game, Blackjack. These simulations provide different perspectives on Blackjack gameplay, enabling users to explore different strategies, scenarios, and outcomes through simulation.

## Overview
This project aims to simulate different strategies of Blackjack and compare the results.

#### Inexperienced Blackjack Simulation: 
Geared towards newcomers to the game, this one simplifies player actions to random choices between hitting and staying (random.choice(['hit', ‘stand']))

#### Simplified Blackjack Simulation (No Splitting):
Player's decisions are based on the value of their hand. The player hits if their hand value is less than 17 and stands otherwise.

#### Blackjack Simulation (Splitting pairs):
This explores the intricacies of splitting hands. It allows users to observe the effects of splitting specific pairs of cards on their chances of winning, losing, or tying against the dealer. Demonstrates a more advanced simulation of Blackjack, incorporating splitting logic and a strategy based on dealer’s card (upcard).

## Blackjack Game Experience
Experience Blackjack excitement with an interactive game interface and stylish design, where your every move determines your fate. 

## Strategies
<img width="500" alt="image" src="https://github.com/Sangyyyy/personal_use/assets/134233430/fdd440c1-b132-4e02-8763-11f388af13c6">

## Flowchart 
<img width="500" alt="image" src="https://github.com/Sangyyyy/personal_use/assets/134233430/da9cef8a-3459-4185-b26d-be8beede8aac">

## Getting Started
To run the Blackjack simulation codes on your local machine, follow these steps:

    1. Ensure you have Python 3.x installed on your system.

    2. Clone this repository or download the individual simulator scripts.

    3. Open a terminal or command prompt and navigate to the directory containing the simulator script you want to run.
    
## Usage
1. Run a simulator script:
```bash
  python script_name.py
```
Replace script_name.py with the desired simulation script.

1. Follow on-screen prompts to set simulation parameters.

2. Results including win, loss, and push percentages will display with a bar chart.

3. For combined strategy plot (100,000 simulations):
```bash
  python Blackjack_combined_plot_100000_sims.py
```
#### Try the Blackjack Simulation Webpage
```bash
1. Download or clone this repository.
2. Open `index.html` in your web browser.
3. Enjoy the interactive Blackjack experience right in your browser.
```
## Result
After running simulations for different blackjack strategies, we gain valuable insights into diverse blackjack scenarios. These results allow us to analyze the effectiveness of various strategies, explore potential outcomes, and better understand how each approach fares in gameplay.

Percentage of Wins: The portion of simulations where the player wins against the dealer.

Percentage of Losses: The portion of simulations where the player loses to the dealer.

Percentage of Ties/Pushes: The portion of simulations where the player's hand ties with the dealer's hand.

These results are visualized using bar charts, showcasing the distribution of different outcomes - Wins, Losses, and Pushes - over the course of the simulations.

The project culminates in a combined plot, comparing the strategies' simulation results. It showcases the distribution of wins, losses, and ties across 100,000 simulations, shedding light on the strategies' relative effectiveness.

#### Blackjack_Inexperienced_player.py
<img width="350" alt="image" src="https://github.com/Sangyyyy/personal_use/assets/134233430/836c1436-583f-4ab0-bd8c-e2d6cd74ae68">

#### Blackjack_simple_logic.py
<img width="350" alt="image" src="https://github.com/Sangyyyy/personal_use/assets/134233430/3fb31ea8-240d-4fe3-93a7-c88c3b910f45">

#### Blackjack_with_splitting.py
<img width="350" alt="image" src="https://github.com/Sangyyyy/personal_use/assets/134233430/ee5265d4-9c8b-4ed0-a051-fae1d4e4b2d4">

#### Blackjack_combined_plot_100000_sims.py
<img width="350" alt="image" src="https://github.com/Sangyyyy/personal_use/assets/134233430/3c994a1f-67b9-44a8-b1b5-52236beba6c3">

## Target Audience
1. Individuals interested in learning Blackjack strategies.
2. Players who want to evaluate potential outcomes using simulations.
3. Enthusiasts who wish to experiment with and modify strategies.
4. Users seeking visual insights into Blackjack strategy outcomes.

## Contributors
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
