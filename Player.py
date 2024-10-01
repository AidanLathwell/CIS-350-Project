from Hand import Hand

class Player:
    def __init__(self, name, balance):

        # String variable that contains players name
        self.name = name

        # Hand class variable object, contains the list for current hand and class functionality
        self.hand = Hand()

        # Int variable to keep track of balance before and after playing games
        self.balance = balance

    """ Method internally called by print message to represent list of cards. // chatgpt """
    def __str__(self):
        return f"Player: {self.name}, Balance: {self.balance}, Hand: {self.hand}"

    def place_bets(self, amount):
        pass

    """ Method that handles cases when a player decides to hit. It will first check that player
        is allowed to hit under given circumstances and update the players hand and value"""
    def hit(self, deck):

        # Check if players current hand value is at least 17
        if self.hand.hand_value <= 17:

            # If hand value is at least 17, check if player is still allowed to hit
            if self.hand.allowed_to_hit is True:

                # Assign variable card to the top card returned from Deck class hit method
                card = deck.hit()

                # Check if deck isn't empty
                if card:
                    self.hand.hand.append(card)    # Call hand method
                    self.hand.calc_hand_value()    # Call hand method

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

        # Check if players current hand value is at least 17
        if self.hand.hand_value <= 17:

            # If hand value is atleast 17, check if player is still allowed to hit
            if self.hand.allowed_to_hit is True:

                # Assign variable card to the top card returned from Deck class hit method
                card = deck.hit()
                self.hand.hand.append(card)    # Call hand method
                self.hand.allowed_to_hit = False
                self.hand.calc_hand_value()    # Call hand method
        return self.hand

    """ Method that handles cases when a player decides to split. """
    def split(self):
        pass

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
