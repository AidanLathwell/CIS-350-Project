from Card import Card

class Hand:
    def __init__(self):

        # List variable that will hold the current cards in your hand
        self.hand = []

        # Int variable to keep track of the current value of all cards combined in hand
        self.hand_value = 0

        # Boolean variable to update if a player can still hit or not
        self.allowed_to_hit = True

        # Boolean to track ability to double
        self.already_hit = False

    """ Method internally called by print message to represent list of cards. // chatgpt """
    def __str__(self):
        return "[" + ", ".join(str(card) for card in self.hand) + "]"

    """  Method used to calculate the value of your hand. The value is re calculated after
         each hand change such as hitting, standing, doubling, and splitting. Assigns 
         calculated value to the self.hand.value variable after each call. """
    def calc_hand_value(self):

        # Temp variable to update with current hand value
        new_hand_value = 0

        """ Int variable to count number of aces in hand. Variable is needed because
            when you have more than one ace, the value of each additional ace changes
            to 1 if hand value would become greater than 21. """
        aces_count = 0
        for card in self.hand:
            if card.value == "Ace":
                aces_count += 1
                if aces_count >= 2:
                    new_hand_value += 1
                elif aces_count == 1:
                    new_hand_value += 11
            elif (card.value == "10" or card.value == "Jack" or card.value == "Queen"
                  or card.value == "King"):
                new_hand_value += 10
            else:
                new_hand_value += int(card.value)

        # Assign new hand value to calculated hand value
        self.hand_value = new_hand_value

        """ Handling multiple aces new hand value (specifically this part of code will be
            used when hitting, doubling, or splitting during the game)"""
        iterations = 0
        hand_value = 0
        temp_card_value = None

        """ This portion of code calculates the new hand value if a hand has more than one ace"""
        if iterations == 0 and len(self.hand) > 2 and aces_count == 1 and new_hand_value > 21:
            for card in self.hand:
                if card.value == "Jack" or card.value == "Queen" or card.value == "King":
                    temp_card_value = 10
                if card.value == "Ace":
                    temp_card_value = 0
                if temp_card_value is not None:
                    hand_value += temp_card_value
                else:
                    hand_value += int(card.value)

                temp_card_value = None

            # Check to see if you need to change ace value to 1 from 11
            if (self.hand_value - hand_value) == 11:
                new_hand_value -= 10

            # Variable to update, prevents portion from happening more than once
            iterations += 1

        """ Only 1 ace in your hand will ever be 11. This portion of code will handle
            re evaluting your hand value if you hit and go over 21 while sitll having
            an ace with the value of 11. """
        already_counted_aces = 0
        if aces_count >= 2 and new_hand_value > 21:
            for card in self.hand:
                if card.value == "Ace":
                    already_counted_aces += 1
                if card.value == "Ace" and already_counted_aces == 1 and new_hand_value > 21:
                    new_hand_value -= 10

        # assign temporary hand value to the self.hand_value variable for global use
        self.hand_value = new_hand_value

    """ This method determines if a player is able to hit or not, and updates the 
        allowed to hit variable accordingly. """
    def calc_ability_to_hit(self):
        aces_count = 0
        temp_hand_value = 0

        # Calculate hand value
        for card in self.hand:
            if card.value == "Ace":
                aces_count += 1
                temp_hand_value += 11
            elif card.value == "King" or card.value == "Jack" or card.value == "Queen":
                temp_hand_value += 10
            else:
                temp_hand_value += int(card.value)

        # Assign ability to hit based on cards in hand and hand value
        if aces_count == 1 and self.hand_value <= 21 and len(self.hand) > 2:
            self.allowed_to_hit = True
        elif aces_count == 1 and self.hand_value == 21 and len(self.hand) == 2:
            self.allowed_to_hit = False
        elif aces_count == 1 and self.hand_value <= 21:
            self.allowed_to_hit = True
        elif aces_count == 1 and self.hand_value > 21:
            if self.hand_value < 21:
                self.allowed_to_hit = True
            else:
                self.allowed_to_hit = False
        elif aces_count >= 2 and self.hand_value > 21:
            self.allowed_to_hit = False
        elif aces_count >= 2 and self.hand_value <= 21:
            self.allowed_to_hit = True
        elif temp_hand_value < 17:
            self.allowed_to_hit = True
        else:
            self.allowed_to_hit = False

    """ Logic for when you create another hand. Cannot access action in player class
        since hand is a hand ovject not a player"""
    def hit(self, deck):

        # If hand value is at least 17, check if player is still allowed to hit
        if self.allowed_to_hit is True:

            # Assign variable card to the top card returned from Deck class hit method
            card = deck.hit()
            self.already_hit = True
            self.hand.append(card)    # Call hand method

        self.calc_hand_value()    # Call hand method
        self.calc_ability_to_hit()

        return self.hand

    """  Method that handles cases when a player decides to stand. It will update the variable
         allowed_to_hit to false because after standing a player is no longer allowed to hit. """
    def stand(self):
        self.allowed_to_hit = False
        return self.hand

    """ Method that handles cases when a player decides to double. It will first check that the
        player is allowed to double under given circumstances and update the players hand and 
        value. """
    def double(self, deck):

        if self.already_hit is False:

            # If hand value is atleast 17, check if player is still allowed to hit
            if self.allowed_to_hit is True:

                # Assign variable card to the top card returned from Deck class hit method
                card = deck.hit()
                self.hand.append(card)

        self.allowed_to_hit = False
        self.calc_hand_value()

        return self.hand