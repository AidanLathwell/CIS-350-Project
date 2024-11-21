from Hand import Hand
from Card import Card

class Dealer:
    def __init__(self):

        # Hand class variable object, contains the list for current hand and class functionality
        self.hand = Hand()

        # Int variable to keep track of casinos balance after games played
        self.balance = 500000000

    """ Method internally called by print message to represent list of cards. """
    def __str__(self):

        """ First half of the if statement will calculate the hand value if the dealer
            only has two cards. It will calculate just the value of the first card so
            that the second card and its value remain hidden. Otherwise, it will display
            normal hand value"""
        hidden_card_value = 0
        if len(self.hand.hand) == 2:
            cards = Hand()
            for card in self.hand.hand:
                cards.hand.append(card)
            display_card = cards.hand[0]
            hidden_card = cards.hand[1]
            if hidden_card.value == "Ace":
                hidden_card_value -= 11
            elif (hidden_card.value == "10" or hidden_card.value == "Jack" or
                  hidden_card.value == "Queen" or hidden_card.value == "King"):
                hidden_card_value -= 10
            else:
                hidden_card_value -= hidden_card.value

            hidden_card_value = self.hand.hand_value + hidden_card_value

            return f"Dealer's Hand: [{display_card}, ?] ({hidden_card_value})"
        else:
            return f"Dealer's Hand: {self.hand} ({self.hand.hand_value})"

    """ Method to carry out a dealers turn in a round. This method is equivalent to the hit
        the player uses. It will add cards to the dealers hand until circumstances occur. """
    def play(self, deck):

        # Check if dealer is allowed to hit
        if self.hand.allowed_to_hit is True:

            # Get top card of the deck and add it to players hand.
            card = deck.hit()
            self.hand.hand.append(card)
            self.hand.calc_hand_value()
            self.hand.calc_ability_to_hit()

        return self.hand


# from Deck import Deck
#
# deck = Deck()
# deck.create_deck()
# deck.shuffle_deck()
#
# test = Dealer()
# test.deal(deck)
# print(test)
# print(test.hand.hand_value)
# print(test.hand.allowed_to_hit)