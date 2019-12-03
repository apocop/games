"""
A simple version of the card game war.
"""

class Card:
    """Represents a card in a deck"""

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
