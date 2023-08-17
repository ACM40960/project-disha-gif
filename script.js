 // Initialize the deck of cards
const deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
let playerHand = [];
let dealerHand = [];
let dealerHiddenValue = null;

// Function to deal a card 
function dealCard() {
    return deck[Math.floor(Math.random() * deck.length)];
}

 // Function to update the player's and dealer's hands
function updateHands() {
    const playerValue = calculateHandValue(playerHand);
    const dealerValue = dealerHiddenValue !== null ? calculateHandValue(dealerHand) : calculateHandValue([dealerHand[0]]);
    
    document.getElementById('player-cards').textContent = playerHand.join(', ');
    document.getElementById('player-value').textContent = `(Total: ${playerValue})`;
    
    if (dealerHiddenValue !== null) {
        document.getElementById('dealer-cards').textContent = dealerHand.join(', ');
        document.getElementById('dealer-value').textContent = `(Total: ${dealerValue})`;
    } else {
        document.getElementById('dealer-cards').textContent = dealerHand[0];
        document.getElementById('dealer-value').textContent = `(Total: ${dealerValue})`;
    }
}

// Function to display the result
function displayResult(result) {
    document.getElementById('result').textContent = result;
}

// Deal button click event
document.getElementById('deal-button').addEventListener('click', () => {
    playerHand = [dealCard(), dealCard()];
    dealerHand = [dealCard(), dealCard()];
    dealerHiddenValue = null;

    updateHands();
    displayResult('');

    // Disable deal button and enable hit and stand buttons
    document.getElementById('deal-button').disabled = true;
    document.getElementById('hit-button').disabled = false;
    document.getElementById('stand-button').disabled = false;
}); 


// Hit button click event
document.getElementById('hit-button').addEventListener('click', () => {
    // Add a card to the player's hand
    playerHand.push(dealCard());

    const playerValue = calculateHandValue(playerHand);
    updateHands();

    // Check if the player busts
    if (playerValue > 21) {
        displayResult('You busted! Dealer wins.');
        endGame();
    }
});

// Stand button click event
document.getElementById('stand-button').addEventListener('click', () => {
    // Reveal the dealer's hidden card and update the dealer's hand
    dealerHiddenValue = calculateHandValue(dealerHand);
    updateHands();

    // Dealer draws cards until hand value reaches 17
    while (calculateHandValue(dealerHand) < 17) {
        dealerHand.push(dealCard());
    }

    updateHands();

    const playerValue = calculateHandValue(playerHand);
    const dealerValue = calculateHandValue(dealerHand);
    
    // Determine the winner and display the result
    if (dealerValue > 21 || dealerValue < playerValue) {
        displayResult('You win!');
    } else if (dealerValue === playerValue) {
        displayResult('It\'s a tie!');
    } else {
        displayResult('Dealer wins.');
    }
    
    // End the game
    endGame();
    
});


// Function to calculate the value of a hand
function calculateHandValue(hand) {
    let value = 0;
    let numAces = 0;

    // Calculate the value of each card in the hand
    for (const card of hand) {
        if (card === 'A') {
            value += 11;
            numAces++;
        } else if (card === 'K' || card === 'Q' || card === 'J') {
            value += 10;
        } else {
            value += parseInt(card);
        }
    }

    // Adjust for aces
    while (value > 21 && numAces > 0) {
        value -= 10;
        numAces--;
    }

    return value;
}

// Function to disable buttons and end the game
function endGame() {
    document.getElementById('hit-button').disabled = true;
    document.getElementById('stand-button').disabled = true;
    document.getElementById('deal-button').disabled = false;
}

// Initial state: Disable hit and stand buttons
endGame();
