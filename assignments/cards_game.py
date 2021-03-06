__author__ = 'PrinceSallu'

import random

SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King"]
PLAYERS = ["North", "East", "South", "West"]

CARDS = 52
CARDS_PER_HAND = 13


def show_hand(hand):
    for card in hand:
        print(RANKS[card % CARDS_PER_HAND], "of",
              SUITS[card // CARDS_PER_HAND], end=" ")


def main():
    deck = list(range(CARDS))

    random.shuffle(deck)

    north = []
    east = []
    south = []
    west = []
    for i in range(13):
        north.append(deck.pop())
        east.append(deck.pop())
        south.append(deck.pop())
        west.append(deck.pop())

    north.sort()
    print ("North has :")
    show_hand(north)
    print("")
    print("")

    east.sort()
    print ("East has :")
    show_hand(east)
    print("")
    print("")

    south.sort()
    print ("South has :")
    show_hand(south)
    print("")
    print("")

    west.sort()
    print ("West has :")
    show_hand(west)
    print("")
    print("")
main()