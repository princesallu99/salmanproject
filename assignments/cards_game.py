__author__ = 'PrinceSallu'

import random

SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King"]
PLAYERS = ["North", "East", "South", "West"]

CARDS = 52
CARDS_PER_HAND = 13


def main():
    # Create a deck as a list of integers from 0 to 51
    deck = list(range(CARDS))

    # Shuffle the deck
    random.shuffle(deck)

    # Show the deck
    print(deck)

    # Pop a card from the end of the deck
    card = deck.pop()
    print(deck)
    print(card)

    # What card is it?
    print("You got the", RANKS[card % CARDS_PER_HAND], "of",
          SUITS[card // CARDS_PER_HAND])


main()
