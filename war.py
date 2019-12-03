"""
A simple version of the card game war.
"""

from random import shuffle

class Card:
    """Represents a card in a deck."""

    suites = [
        'spades',
        'hearts',
        'diamonds',
        'clubs',
    ]

    # Designed so that the index matches the face value of card.
    values = [
        None, None,
        '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'Jack', 'Queen', 'King', 'Ace'
    ]

    def __init__(self, value, suite):
        """value and suite are int"""
        self.value = value
        self.suite = suite

    def __lt__(self, card2):
        if self.value < card2.value:
            return True
        if self.value == card2.value:
            if self.suite < card2.suite:
                return True
            else:
                return False
        return False

    def __gt__(self, card2):
        if self.value > card2.value:
            return True
        if self.value == card2.value:
            if self.suite > card2.suite:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = f'{self.values[self.value]} of {self.suites[self.suite]}'
        return v

class Deck:
    """Create a card deck with 52 cards"""

    def __init__(self):

        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        else:
            return self.cards.pop()

class Player:
    """Keeps track of player stats."""
    def __init__(self, name):
        self.name = name
        self.win = 0
        self.card = None
