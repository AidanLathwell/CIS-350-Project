class Card:
    def __init__(self, suit, value):

        # string variable to represent the suit of the card
        self.suit = suit

        # string variable to represent the value of the card
        self.value = value

    """ Method internally called by print message to represent list of cards in speicific
        string format. """
    def __str__(self):
        return f"{self.value} of {self.suit}"