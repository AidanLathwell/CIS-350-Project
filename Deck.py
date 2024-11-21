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

            suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

            # List containing the 13 different card values
            values = ["Ace", "2", "3"]

            # Iterate through each suit
            for suit in suits:

                # Iterate though each value
                for value in values:
                    new_card = Card(suit, value)
                    self.deck.append(new_card)

    """ Method used to randomize the deck after reaching cut card or starting game. """
    def shuffle_deck(self):
        random.shuffle(self.deck)    # From python docs, built-in function to randomize sequence

    """ Method used to grab the first card of the deck/card at index 0, and return it. """
    def hit(self):

        # check if deck is empty
        if len(self.deck) >= 0:

            # pop the first element out of the list and return it
            return self.deck.pop(0)
        else:
            return None


# test = Deck()
# test.create_deck()
# print(test)
# test.shuffle_deck()
# print(test)    # after shuffle