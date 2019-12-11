"""
A simple version of the card game 'War'.
Based on the code from 
"The Self-Taught Programmer: The Definitive Guide to Programming Professionally "
by Cory Althoff
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

    def draw_card(self):
        if len(self.cards) == 0:
            return
        else:
            return self.cards.pop()


class Player:
    """Keeps track of player stats."""
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None


class Game:
    def __init__(self, debug = False):

        if debug == True:
            name1 = 'Link'
            name2 = 'Zelda'
        else:
            name1 = input('Player 1 name: ')
            name2 = input('Player 2 name: ')

        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def wins(self, winner):
        w = f'{winner} wins this round!'
        print(w)

    def draw(self, player1, player1_card, player2, player2_card):
        d = f'{player1} drew {player1_card}. {player2} drew {player2_card}.'
        print(d)
    
    def play_game(self):
        cards = self.deck.cards
        print('Beginning War!')

        while len(cards) >= 2:
            m = 'q to quit. Any other key to play.'
            response = input(m)
            
            if response == 'q':
                break

            player1_card = self.deck.draw_card()
            player2_card = self.deck.draw_card()

            player1_name = self.player1.name
            player2_name = self.player2.name

            self.draw(player1_name, player1_card, player2_name, player2_card)

            if player1_card > player2_card:
                self.player1.wins += 1
                self.wins(player1_name)
            else:
                self.player2.wins += 1
                self.wins(player2_name)
        
        win = self.winner(self.player1, self.player2)

        if win == 'It was a tie!':
            print(win)
        else:
            print(f'The War is over. {win} wins!')


    def winner(self, player1, player2):
        if player1.wins > player2.wins:
            return player1.name
        elif player1.wins < player2.wins:
            return player2.name
        return 'It was a tie!'


if __name__ == '__main__':
    game = Game()
    game.play_game()