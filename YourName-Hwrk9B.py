import random

# Create a deck of cards with values
def create_deck():
    deck = {
        'Ace of Spades': 11, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5,
        '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10,
        'Jack of Spades': 10, 'Queen of Spades': 10, 'King of Spades': 10,
        'Ace of Hearts': 11, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5,
        '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10,
        'Jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10,
        'Ace of Clubs': 11, '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4, '5 of Clubs': 5,
        '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9, '10 of Clubs': 10,
        'Jack of Clubs': 10, 'Queen of Clubs': 10, 'King of Clubs': 10,
        'Ace of Diamonds': 11, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5,
        '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10,
        'Jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10
    }
    return deck

# Deal a specified number of cards to a hand
def deal_cards(deck, hand, number):
    cards = random.sample(deck.keys(), number)
    for card in cards:
        hand[card] = deck[card]
        del deck[card]

# Calculate the value of a hand considering Aces
def calculate_hand_value(hand):
    value = sum(hand.values())
    num_aces = list(hand.values()).count(11)
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

# Main game logic
def play_blackjack():
    print("Welcome to YourName's Casino - Blackjack Game")

    deck = create_deck()
    player1_hand = {}
    player2_hand = {}

    deal_cards(deck, player1_hand, 2)
    deal_cards(deck, player2_hand, 2)

    while True:
        player1_value = calculate_hand_value(player1_hand)
        player2_value = calculate_hand_value(player2_hand)

        print(f'Player 1\'s Hand: {", ".join(player1_hand.keys())} (Value: {player1_value})')
        print(f'Player 2\'s Hand: {", ".join(player2_hand.keys())} (Value: {player2_value})')

        if player1_value > 21:
            print('Player 2 wins! Player 1 busts!')
            break
        elif player2_value > 21:
            print('Player 1 wins! Player 2 busts!')
            break
        elif player1_value == 21 and player2_value == 21:
            print('It\'s a tie score! Both players have 21!')
            break
        elif player1_value == 21:
            print('Player 1 wins with a score of 21!')
            break
        elif player2_value == 21:
            print('Player 2 wins with a score of 21!')
            break

        choice = input('Player 1, do you want to hit or stand? (h/s): ').lower()
        if choice == 'h':
            deal_cards(deck, player1_hand, 1)
        elif choice == 's':
            while player2_value < 21:
                deal_cards(deck, player2_hand, 1)
                player2_value = calculate_hand_value(player2_hand)

if __name__ == "__main__":
    play_blackjack()
