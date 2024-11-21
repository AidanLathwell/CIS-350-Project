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
        hidden_card_value = 0
        if len(self.hand.hand) == 2:
            cards = Hand()
            for card in self.hand.hand:
                cards.hand.append(card)
            display_card = cards.hand[0]
            hidden_card = cards.hand[1]
            if hidden_card.value == "Ace":
                hidden_card_value -= 11
            elif hidden_card.value == "1":
                hidden_card_value -= 1
            elif hidden_card.value == "2":
                hidden_card_value -= 2
            elif hidden_card.value == "3":
                hidden_card_value -= 3
            elif hidden_card.value == "4":
                hidden_card_value -= 4
            elif hidden_card.value == "5":
                hidden_card_value -= 5
            elif hidden_card.value == "6":
                hidden_card_value -= 6
            elif hidden_card.value == "7":
                hidden_card_value -= 7
            elif hidden_card.value == "8":
                hidden_card_value -= 8
            elif hidden_card.value == "9":
                hidden_card_value -= 9
            elif (hidden_card.value == "10" or hidden_card.value == "Jack" or
                  hidden_card.value == "Queen" or hidden_card.value == "King"):
                hidden_card_value -= 10

            hidden_card_value = self.hand.hand_value + hidden_card_value

            return (f"Dealer's Hand: [{display_card}, ?] ({hidden_card_value})")
        else:
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
                aces_count = 0
                other_cards = []
                other_card_value_total = 0
                for card in self.hand.hand:
                    if card.value == "Ace":
                        aces_count += 1
                    elif card.value != "Ace":
                        other_cards.append(card)
                        if card.value == "Jack" or card.value == "Queen" or card.value == "King":
                            other_card_value_total += 10
                        else:
                            other_card_value_total += int(card.value)

                if (aces_count == 1 and len(self.hand.hand) == 2 and
                        self.hand.hand_value == 21):
                    self.hand.allowed_to_hit = False
                elif aces_count == 1 and self.hand.hand_value < 21:
                    self.hand.allowed_to_hit = True
                elif aces_count > 1 and other_card_value_total + (1 * aces_count) < 21:
                    self.hand.allowed_to_hit = True
                elif self.hand.hand_value >= 17:
                    self.hand.allowed_to_hit = False
                else:
                    self.hand.allowed_to_hit = True

        else:

            # Assign variable card to the top card returned from Deck class hit method
            card = deck.hit()

            # Check if deck isn't empty
            if card:
                self.hand.hand.append(card)  # Call hand method
                self.hand.calc_hand_value()  # Call hand method

            """ Check if hand value is now 17 or greater after hitting. If it is,
                then update allowed_to_hit variable to false since you can no longer hit. """
            aces_count = 0
            other_cards = []
            cut_list = []
            other_card_value_total = 0
            for card in self.hand.hand:
                if card.value == "Ace":
                    aces_count += 1
                elif card.value == "Cut Card":
                    cut_list.append(card)
                elif card.value != "Ace":
                    other_cards.append(card)
                    if card.value == "Jack" or card.value == "Queen" or card.value == "King":
                        other_card_value_total += 10
                    else:
                        other_card_value_total += int(card.value)

            if (aces_count == 1 and len(self.hand.hand) == 2 and
                    self.hand.hand_value == 21):
                self.hand.allowed_to_hit = False
            elif aces_count == 1 and self.hand.hand_value < 21:
                self.hand.allowed_to_hit = True
            elif aces_count > 1 and other_card_value_total + (1 * aces_count) < 21:
                self.hand.allowed_to_hit = True
            elif self.hand.hand_value >= 17:
                self.hand.allowed_to_hit = False
            else:
                self.hand.allowed_to_hit = True

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