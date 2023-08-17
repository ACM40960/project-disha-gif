# SIMULATE SINGLE DECK BLACKJACK 
The Blackjack Simulation project offers a collection of Python scripts designed to allow users to simulate and analyze various aspects of the classic card game, Blackjack. These simulations provide different perspectives on Blackjack gameplay, enabling users to explore different strategies, scenarios, and outcomes through simulation.

## Overview
This project aims to simulate different player strategies of Blackjack and compare the results.

#### Inexperienced Blackjack Simulation: 
Geared towards newcomers to the game, this one simplifies player actions to random choices between hitting and staying (random.choice(['hit', ‘stand']))

#### Simplified Blackjack Simulation (No Splitting):
Player's decisions are based on the value of their hand. The player hits if their hand value is less than 17 and stands otherwise.

#### Blackjack Simulation (Splitting pairs):
Demonstrates a more advanced simulation of Blackjack, incorporating splitting logic and a strategy based on dealer’s card (upcard). It allows users to observe the effects of splitting specific pairs of cards on their chances of winning, losing, or tying against the dealer. 

## Blackjack Game Experience
Experience Blackjack excitement with our interactive game interface and stylish design, where your every move determines your fate.

## Player Strategies 
<img width="530" alt="Strategies" src="https://github.com/Sangyyyy/personal_use/assets/134233430/a8fdd9c6-b004-489d-bd76-5bff0c01c6b6">

## Flowchart 
<img width="900" alt="Flowchart" src="https://github.com/Sangyyyy/personal_use/assets/134233430/750b55fb-e701-4a75-9579-4ae96b27f48c">

## Files guide
1. Blackjack_Inexperienced_player.py : Inexperienced player strategy
2. Blackjack_simple_logic.py : Simple player strategy
3. Blackjack_with_splitting.py : Complex (with splitting) player strategy
4. Blackjack_combined_plot_10000_sims.py : Combined results plotted together
5. index.html : Blackjack interactive game webpage
6. script.js : javascript for the webpage
7. style.css : CSS for the webpage

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
<img width="550" alt="Inexperienced" src="https://github.com/Sangyyyy/personal_use/assets/134233430/c815b7c3-6df1-41e0-84a6-7b54dbdede44">

#### Blackjack_simple_logic.py
<img width="550" alt="Simple" src="https://github.com/Sangyyyy/personal_use/assets/134233430/2758ce9e-164e-4271-8030-cef48706438a">

#### Blackjack_with_splitting.py
<img width="550" alt="Spiltting" src="https://github.com/Sangyyyy/personal_use/assets/134233430/97657cc7-35f0-4e36-b471-3bef9342088a">

#### Blackjack_combined_plot_100000_sims.py
<img width="850" alt="Combined" src="https://github.com/Sangyyyy/personal_use/assets/134233430/c4ea68f0-9adc-4a70-827e-5c41ad414ac3">

1. Inexperienced player strategy - randomness often leads to unfavourable decisions; player tends to bust more frequently (high loss percentage) and make suboptimal decisions (lower win percentage).
2. The simple logic strategy increases the player's chances of having a stronger hand but also exposes them to a higher risk of busting. Higher win percentage – due to player's tendency to reach higher hand values. Higher tie percentage - due to the simple strategy leading to similar hand values more often.
3. Complex logic (with Splitting Strategy) has higher Win Percentage; the complex strategy likely makes better use of opportunities to split pairs, which can result in stronger hands - more potential wins. More risks involved - the strategy might take calculated risks that lead to busting. For instance, hitting on certain hands could backfire, contributing to a higher loss percentage. The complex strategy likely prioritizes actions that avoid ties by actively seeking wins or losses (lower tie percentage).

## Target Audience
1. Individuals interested in learning Blackjack strategies.
2. Players who want to evaluate potential outcomes using simulations.
3. Enthusiasts who wish to experiment with and modify strategies.
4. Users seeking visual insights into Blackjack strategy outcomes.

## Contributors
Pull requests are welcome. For major changes, please open an issue to discuss.

## Contact
This project was a collaborative submission to UCD School of Mathematics. To reach out to us - disha.satyanarayan@ucdconnect.ie or sangeeta.panigrahi@ucdconnect.ie

