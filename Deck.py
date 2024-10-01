from Card import Card
import random

class Deck:
    def __init__(self):

        # List variable that will hold the 312 cards in the current deck
        self.deck = []

    """ Method internally called by print message to represent list of cards. // chatgpt """
    def __str__(self):
        return "[" + ", ".join(str(card) for card in self.deck) + "]"

    """ Method used to generate the original deck of cards when starting a blackjack game. 
        The method loops 6 times to create 6 decks as most casinos use a 312 card deck. It 
        then adds each card to the self.deck list after creation. """
    def create_deck(self):

        # For loop that will iterate 6 times
        for deck in range(6):

            # List containing the 4 types of suits
            suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

            # List containing the 13 different card values
            values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

            # Iterate through each suit
            for suit in suits:

                # Iterate though each value
                for value in values:
                    new_card = Card(suit, value)
                    self.deck.append(new_card)

    """ Method used to randomize the deck after reaching cut card or starting game. """
    def shuffle_deck(self):
        random.shuffle(self.deck)    # From python docs, built-in function to randomize sequence

    def hit(self):
        if len(self.deck) >= 0:
            return self.deck.pop(0)
        else:
            return None
