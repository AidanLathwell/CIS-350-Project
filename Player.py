from Hand import Hand
from Card import Card

class Player:
    def __init__(self, name, balance):

        # String variable that contains players name
        self.name = name

        # Hand class variable object, contains the list for current hand and class functionality
        self.hand = Hand()

        # Int variable to keep track of balance before and after playing games
        self.balance = balance

    """ Method internally called by print message to represent list of cards. """
    def __str__(self):
        return f"{self.name}'s Hand: {self.hand} ({self.hand.hand_value})"

    """ Method that handles cases when a player decides to hit. It will check if the player
        is allowed to hit if their hand is larger than 17 because of aces, otherwise it will
        do a normal hit. """
    def hit(self, deck):

        # If hand value is at least 17, check if player is still allowed to hit
        if self.hand.allowed_to_hit is True:

            # Assign variable card to the top card returned from Deck class hit method
            card = deck.hit()
            self.hand.already_hit = True

            # Check if deck isn't empty
            if card:
                self.hand.hand.append(card)    # Call hand method

        # Update hand value and ability to hit
        self.hand.calc_hand_value()
        self.hand.calc_ability_to_hit()

        return self.hand

    """  Method that handles cases when a player decides to stand. It will update the variable
         allowed_to_hit to false because after standing a player is no longer allowed to hit. """
    def stand(self):
        self.hand.allowed_to_hit = False
        return self.hand

    """ Method that handles cases when a player decides to double. It will first check that the
        player is allowed to double under given circumstances and update the players hand and 
        value. """
    def double(self, deck):

        # Check that a player has not previously hit
        if self.hand.already_hit is False:

            # Check if hand is allowed to be hit
            if self.hand.allowed_to_hit is True:

                # Assign variable card to the top card returned from Deck class hit method
                card = deck.hit()
                self.hand.hand.append(card)

                # Manually assign hand ability to hit, you can not hit after doubling
                self.hand.already_hit = True
                self.hand.allowed_to_hit = False

        self.hand.calc_hand_value()

        return self.hand

# from Deck import Deck
#
# deck = Deck()
# deck.create_deck()
# deck.shuffle_deck()
#
# test = Player("Logan", 100)
# print(test)
# test.hit(deck)
# print(test)
# test.hit(deck)
# print(test)
# test.hit(deck)
# print(test)
# test.hit(deck)
# test.hit(deck)
# print(test)
#
# print(test.hand.hand_value)
# print(test.hand.allowed_to_hit)