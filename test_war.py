import war

def test_card():
    """Test cards"""
    # value, suite, strig
    card_variables = [
        (2, 0, '2 of spades'),
        (3, 1, '3 of hearts'),
        (10, 2, '10 of diamonds'),
        (12, 3, 'Queen of clubs'),
        (13, 1, 'King of hearts'),
    ]

    for value, suite, card_name in card_variables:
        assert war.Card(value, suite).__repr__() == card_name
