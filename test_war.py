import war

class TestCard:
    def test_card_names(self):
        """Test cards"""
        # value, suite, name.
        variables = [
            (2, 0, '2 of spades'),
            (3, 1, '3 of hearts'),
            (10, 2, '10 of diamonds'),
            (12, 3, 'Queen of clubs'),
            (13, 1, 'King of hearts'),
        ]

        for value, suite, card_name in variables:
            assert war.Card(value, suite).__repr__() == card_name


    def test_card_gt(self):
        "Test 'Greater Than' magic method."

        variables = [
            # Test value Greater than.
            (3, 0, 2, 0, True),
            (10, 0, 5, 0, True),
            (2, 3, 8, 2, False),
            (4, 0, 11, 1, False),
            (4, 2, 1, 3, True),
            # Test suite greater than.
            (4, 5, 4, 3, True),
            (10, 3, 10, 0, True),
            (8, 1, 8, 2, False),
            (12, 1, 12, 3, False),
        ]

        for x in variables:
            assert (war.Card(x[0], x[1]) > war.Card(x[2], x[3])) == x[4]

    def test_card_lt(self):
        "Test 'Less Than' magic method."

        variables = [
            # Test value Less Than.
            (3, 0, 2, 0, False),
            (10, 0, 5, 0, False),
            (2, 3, 8, 2, True),
            (4, 0, 11, 1, True),
            (4, 2, 1, 3, False),
            # Test suite Less Than.
            (4, 5, 4, 3, False),
            (10, 3, 10, 0, False),
            (8, 1, 8, 2, True),
            (12, 1, 12, 3, True),
        ]

        for x in variables:
            assert (war.Card(x[0], x[1]) < war.Card(x[2], x[3])) == x[4]


class TestDeck:
    def test_deck_has_52_cards(self):
        """Check that a deck as 52 cards."""
        deck = war.Deck()
        assert len(deck.cards) == 52

    def test_deck_cards(self):
        """Verify that there is no cards with None value in a deck."""

        deck = war.Deck()
        for card in deck.cards:
            assert card.value != None

    def test_deck_card_suites(self):
        """Test that there are only 4 suites."""

        deck = war.Deck()
        for card in deck.cards:
            assert 0 <= card.suite <= 3



