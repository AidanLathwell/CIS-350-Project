class Hand:
    def __init__(self):

        # List variable that will hold the current cards in your hand
        self.hand = []

        # Int variable to keep track of the current value of all cards combined in hand
        self.hand_value = 0

        # Boolean variable to update if a player can still hit or not
        self.allowed_to_hit = True

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
                    if (new_hand_value + 11) > 21:
                        new_hand_value += 1
                    else:
                        new_hand_value += 11
                elif aces_count == 1:
                    if (new_hand_value + 11) > 21:
                        new_hand_value += 1
                    else:
                        new_hand_value += 11
                else:
                    new_hand_value += 11
            elif card.value == "1":
                new_hand_value += 1
            elif card.value == "2":
                new_hand_value += 2
            elif card.value == "3":
                new_hand_value += 3
            elif card.value == "4":
                new_hand_value += 4
            elif card.value == "5":
                new_hand_value += 5
            elif card.value == "6":
                new_hand_value += 6
            elif card.value == "7":
                new_hand_value += 7
            elif card.value == "8":
                new_hand_value += 8
            elif card.value == "9":
                new_hand_value += 9
            elif (card.value == "10" or card.value == "Jack" or card.value == "Queen"
                  or card.value == "King"):
                new_hand_value += 10

        if len(self.hand) > 2 and aces_count == 1 and new_hand_value > 21:
            new_hand_value -= 10

        """ NEED code here to handle situations where there is more than 1 ace in the hand
            and the hand value is greater than 21. This is because one of the aces was assigned
            a value of 11 prior to going over the 21 limit but it now changes to a 1 if it 
            would be less than 21 """
        # Implement code here

        # assign temporary hand value to the self.hand_value variable for global use
        self.hand_value = new_hand_value
        return self.hand_value