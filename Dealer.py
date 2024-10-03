from Hand import Hand

class Dealer:
    def __init__(self):

        # Hand class variable object, contains the list for current hand and class functionality
        self.hand = Hand()

        # Int variable to keep track of casinos balance after games played
        self.balance = 50000000

    """ Method internally called by print message to represent list of cards. """
    def __str__(self):
        return f"Dealer's Hand: {self.hand} ({self.hand.hand_value})"

    """ Method to carry out a dealers turn in a round. This method is equivalent to the hit
        the player uses. It will add cards to the dealers hand until circumstances occur. """
    def play(self, deck):

        # Check if hand value is greater than or equal 17
        if self.hand.hand_value >= 17:

            # Check that a player is allowed to hit if there hand is over 17
            if self.hand.allowed_to_hit is True:

                # Assign card variable to the card returned in the Deck class hit method
                card = deck.hit()

                # Check if deck isn't empty by verifying you receieved a card
                if card:
                    self.hand.hand.append(card)    # Call hand method
                    self.hand.calc_hand_value()    # Call hand method

                """ Check if hand value is now 17 or greater after hitting. If it is,
                    then update allowed_to_hit variable to false since you can no longer hit. """
                if self.hand.hand_value >= 17:
                    self.hand.allowed_to_hit = False
        else:

            # Assign variable card to the top card returned from Deck class hit method
            card = deck.hit()

            # Check if deck isn't empty
            if card:
                self.hand.hand.append(card)  # Call hand method
                self.hand.calc_hand_value()  # Call hand method

            """ Check if hand value is now 17 or greater after hitting. If it is,
                then update allowed_to_hit variable to false since you can no longer hit. """
            if self.hand.hand_value >= 17:
                self.hand.allowed_to_hit = False

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