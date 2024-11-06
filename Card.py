class Card:
    def __init__(self, suit, value):

        # String variable to represent the suit of the card
        self.suit = suit

        # String variable to represent the value of the card
        self.value = value

    """ Method internally called by print message to represent list of cards. """
    def __str__(self):
        return f"{self.value} of {self.suit}"