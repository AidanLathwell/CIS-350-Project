from Deck import Deck
from Player import Player
from Dealer import Dealer

class Blackjack:
    def __init__(self):

        # Deck class variable object, contains the deck list and deck class functionality
        self.deck = Deck()

        # String variable taken as input for players name (for player class)
        name = str(input("Enter player name: "))

        # Integer variable taken as input for players balance (for player class)
        balance = int(input("Enter money balance(int): "))

        # Player class variable object, contains the hand list and hand class functionality
        self.player = Player(name, balance)

        # Dealer class variable object, contains the hand lsit and hand class functionality
        self.dealer = Dealer()

        # Int variable to track the current wager amount of a hand/round
        self.bet_amount = 0

        # Boolean variable to be updated based upon the winner of a round
        self.winner = None

    """ Method used to start the blackjack game, it will call all other methods to run the game. """
    def start(self):
        self.deck.create_deck()
        self.deck.shuffle_deck()
        self.deal()
        self.player_turn()
        self.dealer_turn()
        self.determine_winner()

    """ Method used to deal first 2 cards to the dealer and player hands. """
    def deal(self):

        """ Draw 4 card objects from the deck and assign them individually to each of the 4 variables """
        card1 = self.deck.hit()
        card2 = self.deck.hit()
        card3 = self.deck.hit()
        card4 = self.deck.hit()

        # Check that card exists, if it does add it to player hand and update hand value
        if card1:
            self.player.hand.hand.append(card1)
        self.player.hand.calc_hand_value()

        # Check that card exists, if it does add it to dealer hand and update hand value
        if card2:
            self.dealer.hand.hand.append(card2)
        self.dealer.hand.calc_hand_value()

        # Check that card exists, if it does add it to player hand and update hand value
        if card3:
            self.player.hand.hand.append(card3)
        self.player.hand.calc_hand_value()

        # Check that card exists, if it does add it to dealer hand and update hand value
        if card4:
            self.dealer.hand.hand.append(card4)
        self.dealer.hand.calc_hand_value()

        """ This chunk of statements will determine if the player is allowed to hit based
            off of their first 2 cards dealt and updates the respective boolean variables. """
        if self.player.hand.hand_value >= 17:
            aces_count = 0
            for card in self.player.hand.hand:
                if card.value == "Ace":
                    aces_count += 1
                    self.player.hand.allowed_to_hit = True
                if aces_count == 0:
                    self.player.hand.allowed_to_hit = False
                elif aces_count == 1 and self.player.hand.hand_value == 21:
                    self.player.hand.allowed_to_hit = False

        """ This chunk of statements will determine if the dealer is allowed to hit based
            off of their first 2 cards dealt and updates the respective boolean variables. """
        if self.dealer.hand.hand_value >= 17:
            aces_count = 0
            for card in self.dealer.hand.hand:
                if card.value == "Ace":
                    aces_count += 1
                    self.dealer.hand.allowed_to_hit = True
                if aces_count == 0:
                    self.dealer.hand.allowed_to_hit = False
                elif aces_count == 1 and self.dealer.hand.hand_value == 21:
                    self.dealer.hand.allowed_to_hit = False

        print(f"{self.player} Vs. {self.dealer}")

    """ Method that handles the logic for the players turn. Will take an input and perform
        specified decision by the player. """
    def player_turn(self):

        """ This while loop will iterate for the players entire hand. It will assign a players
            input to the variable "decision" and then perform a hit, stand, double, or split
            based on whichever input the variable says."""
        while self.player.hand.allowed_to_hit is True:

            # String variable to assign to the players input
            decision = str(input("What would you like to do?: "))

            # If statement that handles logic when a player decides to hit
            if decision == "H" or decision == "h" or decision == "hit" or decision == "Hit":
                self.player.hit(self.deck)
                print(f"{self.player} Vs. {self.dealer}")

            # If statement that handles logic when a player decides to stand
            elif decision == "S" or decision == "s" or decision == "stand" or decision == "Stand":
                self.player.stand()
                print(f"{self.player} Vs. {self.dealer}")

            # If statement that handles logic when a player decides to double
            elif decision == "D" or decision == "d" or decision == "double" or decision == "Double":
                self.player.double(self.deck)
                print(f"{self.player} Vs. {self.dealer}")

            # NEED CODE HERE FOR SPLITTING WHEN IMPLEMENTED
            # If statement that handles logic when a player decides to double
            # elif decision == "split" or decision == "Split":
            #     same_count = 0
            #     check_value_list = []
            #     for card in self.player.hand.hand[1:]:
            #         if same_count == 0:
            #             same_count += 1
            #             check_value_list.append(card.value)
            #         elif same_count == 1:
            #             for value in check_value_list:
            #                 if card.value == value:
            #
            #                     split_player_hand = self.player.split(self.deck)
            #
            #                     new_card = deck.hit()
            #                     if new_card:
            #                         self.player.hand.append(new_card)
            #                         self.player.hand.calc_hand_value()
            #
            #                     print(f"{self.player}, {split_player_hand} Vs. {self.dealer}")

    """ Method that handles the logic for the dealers turn. """
    def dealer_turn(self):

        # If statement to check if a player has blackjack (dealer doesn't play if they do)
        if self.player.hand.hand_value == 21 and len(self.player.hand.hand) == 2:
            return

        # Check if the players hand is 21 or lower (dealer doesn't need to play if player busted)
        if self.player.hand.hand_value <= 21 and len(self.player.hand.hand) >= 2:

            """ This while loop will iterate for the dealers entire hand. While the dealer is
                still allowed to hit, it will call the dealers play method to perform a hit. """
            while self.dealer.hand.allowed_to_hit is True:
                self.dealer.play(self.deck)
                print(f"{self.player} Vs. {self.dealer}")

    """ Method that will determine the winner of the game after both the player and dealer
        have completed their hands(rounds). """
    def determine_winner(self):
        if 21 >= self.player.hand.hand_value > self.dealer.hand.hand_value:
            self.winner = self.player
        elif 21 >= self.dealer.hand.hand_value > self.player.hand.hand_value:
            self.winner = self.dealer
        elif self.player.hand.hand_value > 21 >= self.dealer.hand.hand_value:
            self.winner = self.dealer
        elif self.dealer.hand.hand_value > 21 >= self.player.hand.hand_value:
            self.winner = self.player
        elif self.player.hand.hand_value == self.dealer.hand.hand_value:
            self.winner = None

        if self.winner == self.player:
            print(f"{self.player.name} wins!")
        elif self.winner == self.dealer:
            print("Dealer wins!")
        else:
            print("Push")

        return self.winner


test = Blackjack()
test.start()