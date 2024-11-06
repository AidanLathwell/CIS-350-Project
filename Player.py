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

        # Boolean value to check if a player already hit this turn (for tracking doubles)
        self.already_hit = False

    """ Method internally called by print message to represent list of cards. """
    def __str__(self):
        return f"{self.name}'s Hand: {self.hand} ({self.hand.hand_value})"

    """ Method that will handle placing bets and the amount for each round """
    def place_bets(self, amount):
        pass

    """ Method that handles cases when a player decides to hit. It will check if the player
        is allowed to hit if their hand is larger than 17 because of aces, otherwise it will
        do a normal hit. """
    def hit(self, deck):

        # Check if players current hand value is at least 17
        if self.hand.hand_value >= 17:

            # If hand value is at least 17, check if player is still allowed to hit
            if self.hand.allowed_to_hit is True:

                # Assign variable card to the top card returned from Deck class hit method
                card = deck.hit()
                self.already_hit = True

                # Check if deck isn't empty
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
            self.already_hit = True

            # Check if deck isn't empty
            if card:
                self.hand.hand.append(card)  # Call hand method
                self.hand.calc_hand_value()  # Call hand method

            """ Check if hand value is now 17 or greater after hitting. If it is,
                then update allowed_to_hit variable to false since you can no longer hit. """
            if self.hand.hand_value >= 17:
                self.hand.allowed_to_hit = False

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

        if self.already_hit is False:
            # Check if players current hand value is at least 17
            if self.hand.hand_value <= 17:

                # If hand value is atleast 17, check if player is still allowed to hit
                if self.hand.allowed_to_hit is True:

                    # Assign variable card to the top card returned from Deck class hit method
                    card = deck.hit()
                    self.already_hit = True
                    self.hand.hand.append(card)    # Call hand method
                    self.hand.allowed_to_hit = False
                    self.hand.calc_hand_value()    # Call hand method
        else:
            print("Server: You have already hit, you can not double.")

        return self.hand

    """ Method that handles cases when a player decides to split. """
    def split(self, deck):

        if self.already_hit is False:

            new_hand = Hand()
            split_card = self.hand.hand.pop(1)
            new_hand.hand.append(split_card)

            # add card to new hand
            card_for_hand = deck.hit()
            if card_for_hand:
                new_hand.hand.append(card_for_hand)
                new_hand.calc_hand_value()

            if new_hand.hand_value >= 17:
                new_hand.allowed_to_hit = False

        else:
            print("Server: Cannot split without identical cards.")

        return new_hand


    """ Method that returns a boolean value based on if the players hand busted or not. """
    def check_bust(self):

        # Temp variable to store boolean result for if a player busted, originally set to false
        bust = False

        # Check if the players hand is greater than 21, if so, update bust variable to True
        if self.hand.hand_value > 21:
            bust = True
        return bust

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
# print(test.check_bust())