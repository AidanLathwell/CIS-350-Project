from Deck import Deck
from Player import Player
from Dealer import Dealer

class Blackjack:
    def __init__(self):

        """ Deck class variable object, contains the deck list and deck class functionality"""
        self.deck = Deck()

        """ Player class variable object, contains the hand list and hand class functionality"""
        self.player = Player("Player", 1000)

        """ Dealer class variable object, contains the hand lsit and hand class functionality"""
        self.dealer = Dealer()

        """ Int variable to track the current wager amount of a hand/round"""
        self.bet_amount = 10

        """ Boolean variable to be updated based upon the winner of a round"""
        self.winner = None
        self.winner2 = None

        """ variable to handle winner results when more than 1 hand"""
        self.hand_count = 1

        """ variable to help determine winner for second hand"""
        self.new_hand_split_hand_value_tracker = 0

        """ variable to handle play again instances instead of restarting program"""
        self.game_over = False

    """ Method used to start the blackjack game, it will call all other methods to run the game. """
    def start(self):
        while (self.bet_amount > self.player.balance or self.bet_amount > self.dealer.balance
                or self.bet_amount <=0):
            self.bet_amount = int(input("Server: Wagers cannot exceed your wallet or be less than 0.\n"
                                        "Enter wager amount: "))
        if self.bet_amount <= self.player.balance and self.bet_amount <= self.dealer.balance:
            self.deck.create_deck()
            self.deck.shuffle_deck()
            self.deal()
            self.player_turn()
            self.dealer_turn()
            self.determine_winner()
            #self.play_again()

    """ Method used to deal first 2 cards to the dealer and player hands. """
    def deal(self):

        """ Draw 4 card objects from the deck and assign them individually to each of the 4 variables """
        card1 = self.deck.hit()
        card2 = self.deck.hit()
        card3 = self.deck.hit()
        card4 = self.deck.hit()

        """ Check that card exists, if it does add it to player hand and update hand value"""
        if card1:
            self.player.hand.hand.append(card1)
        self.player.hand.calc_hand_value()

        """ Check that card exists, if it does add it to dealer hand and update hand value"""
        if card2:
            self.dealer.hand.hand.append(card2)
        self.dealer.hand.calc_hand_value()

        """ Check that card exists, if it does add it to player hand and update hand value"""
        if card3:
            self.player.hand.hand.append(card3)
        self.player.hand.calc_hand_value()

        """ Check that card exists, if it does add it to dealer hand and update hand value"""
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
        new_hand_split = None
        decision_count = 0
        while self.player.hand.allowed_to_hit is True:

            """ String variable to assign to the players input"""
            decision = str(input("What would you like to do?: "))

            """ If statement that handles logic when a player decides to hit"""
            if decision == "H" or decision == "h" or decision == "hit" or decision == "Hit":
                self.player.hit(self.deck)
                decision_count += 1

                if self.hand_count == 1:
                    print(f"{self.player} Vs. {self.dealer}")

                elif self.hand_count == 2:
                    print(f"{self.player} Vs. {self.dealer}")
                    print(f"{self.player.name}'s Hand 2: {new_hand_split} ({new_hand_split.hand_value}) Vs. {self.dealer}")

            """ If statement that handles logic when a player decides to stand"""
            elif decision == "S" or decision == "s" or decision == "stand" or decision == "Stand":
                self.player.stand()
                decision_count += 1

                if self.hand_count == 1:
                    print(f"{self.player} Vs. {self.dealer}")

                elif self.hand_count == 2:
                    print(f"{self.player} Vs. {self.dealer}")
                    print(f"{self.player.name}'s Hand 2: {new_hand_split} ({new_hand_split.hand_value}) Vs. {self.dealer}")

            """ If statement that handles logic when a player decides to double"""
            elif decision == "D" or decision == "d" or decision == "double" or decision == "Double":
                self.player.double(self.deck)
                decision_count += 1

                if self.hand_count == 1:
                    print(f"{self.player} Vs. {self.dealer}")

                elif self.hand_count == 2:
                    print(f"{self.player} Vs. {self.dealer}")
                    print(f"{self.player.name}'s Hand 2: {new_hand_split} ({new_hand_split.hand_value}) Vs. {self.dealer}")

            """ If statement that handles logic when a player decides to split"""
            elif decision == "SP" or decision == "sp" or decision == "split" or decision == "Split":
                self.hand_count += 1
                new_hand_split = self.player.split(self.deck)
                self.player.hit(self.deck)
                decision_count += 1
                print(f"{self.player} Vs. {self.dealer}")
                print(f"{self.player.name}'s Hand 2: {new_hand_split} ({new_hand_split.hand_value}) Vs. {self.dealer}")

        """ This portion of code handles when a player finished their first hand but still has to 
            play out their second hand. """
        if new_hand_split is not None and self.player.hand.allowed_to_hit is False:
            while new_hand_split.allowed_to_hit is True:

                """ String variable to assign to the players input"""
                decision = str(input("What would you like to do with your second hand?: "))

                """ If statement that handles logic when a player decides to hit"""
                if decision == "H" or decision == "h" or decision == "hit" or decision == "Hit":
                    new_hand_split.hit(self.deck)
                    decision_count += 1
                    print(f"{self.player.name}'s Hand {new_hand_split} Vs. {self.dealer}")

                """ If statement that handles logic when a player decides to stand"""
                elif decision == "S" or decision == "s" or decision == "stand" or decision == "Stand":
                    new_hand_split.stand()
                    decision_count += 1
                    print(f"{self.player.name}'s Hand {new_hand_split} Vs. {self.dealer}")

                """ If statement that handles logic when a player decides to double"""
                elif decision == "D" or decision == "d" or decision == "double" or decision == "Double":
                    new_hand_split.double(self.deck)
                    decision_count += 1
                    print(f"{self.player.name}'s Hand {new_hand_split} Vs. {self.dealer}")

                # # If statement that handles logic when a player decides to split
                # elif decision == "SP" or decision == "sp" or decision == "split" or decision == "Split":
                #     hand_count += 1
                #     new_hand_split = self.player.split(self.deck)
                #     self.player.hit(self.deck)
                #     decision_count += 1
                #     print(f"{self.player} Vs. {self.dealer}")
                #     print(f"{self.player.name}'s Hand {new_hand_split} ({new_hand_split.hand_value}) Vs. {self.dealer}")

        if self.hand_count == 2:
            self.new_hand_split_hand_value_tracker += new_hand_split.hand_value

        if decision_count == 0:
            print("Server: Hand value >= 17. Auto stand")

    """ Method that handles the logic for the dealers turn. """
    def dealer_turn(self):

        """ If statement to check if a player has blackjack (dealer doesn't play if they do)"""
        if self.player.hand.hand_value == 21 and len(self.player.hand.hand) == 2:
            return

        """ Check if the players hand is 21 or lower (dealer doesn't need to play if player busted)"""
        if self.player.hand.hand_value <= 21 and len(self.player.hand.hand) >= 2:

            """ This while loop will iterate for the dealers entire hand. While the dealer is
                still allowed to hit, it will call the dealers play method to perform a hit. """
            while self.dealer.hand.allowed_to_hit is True:
                self.dealer.play(self.deck)
                print(f"{self.player} Vs. {self.dealer}")

    """ Method that will determine the winner of the game after both the player and dealer
        have completed their hands(rounds). It will also assign payouts to both player and 
        dealer. """
    def determine_winner(self):

        """ hand 1 winner"""
        if 21 >= self.player.hand.hand_value > self.dealer.hand.hand_value:
            self.winner = self.player
            self.player.balance += self.bet_amount
            self.dealer.balance -= self.bet_amount
        elif 21 >= self.dealer.hand.hand_value > self.player.hand.hand_value:
            self.winner = self.dealer
            self.player.balance -= self.bet_amount
            self.dealer.balance += self.bet_amount
        elif self.player.hand.hand_value > 21 >= self.dealer.hand.hand_value:
            self.winner = self.dealer
            self.player.balance -= self.bet_amount
            self.dealer.balance += self.bet_amount
        elif self.dealer.hand.hand_value > 21 >= self.player.hand.hand_value:
            self.winner = self.player
            self.player.balance += self.bet_amount
            self.dealer.balance -= self.bet_amount
        elif self.player.hand.hand_value == self.dealer.hand.hand_value:
            self.winner = None

        """ hand 2 winner"""
        if self.hand_count == 2:
            if 21 >= self.new_hand_split_hand_value_tracker > self.dealer.hand.hand_value:
                self.winner2 = self.player
                self.player.balance += self.bet_amount
                self.dealer.balance -= self.bet_amount
            elif 21 >= self.dealer.hand.hand_value > self.new_hand_split_hand_value_tracker:
                self.winner2 = self.dealer
                self.player.balance -= self.bet_amount
                self.dealer.balance += self.bet_amount
            elif self.new_hand_split_hand_value_tracker > 21 >= self.dealer.hand.hand_value:
                self.winner2 = self.dealer
                self.player.balance -= self.bet_amount
                self.dealer.balance += self.bet_amount
            elif self.dealer.hand.hand_value > 21 >= self.new_hand_split_hand_value_tracker:
                self.winner2 = self.player
                self.player.balance += self.bet_amount
                self.dealer.balance -= self.bet_amount
            elif self.new_hand_split_hand_value_tracker == self.dealer.hand.hand_value:
                self.winner2 = None

        """ handle winner results if only 1 hand"""
        if self.winner2 is None:
            if self.winner == self.player:
                print(f"{self.player.name} wins!")
            elif self.winner == self.dealer:
                print("Dealer wins!")
            else:
                print("Push")

        """ hand winner results if 2 hands"""
        if self.winner2 is not None:
            if self.winner == self.player:
                print(f"{self.player.name} wins hand 1!")
            elif self.winner == self.dealer:
                print("Dealer wins hand 1!")
            elif self.winner is None:
                print("Hand 1 resulted in a push.")

            if self.winner2 == self.player:
                print(f"{self.player.name} wins hand 2!")
            elif self.winner2 == self.dealer:
                print("Dealer wins hand 2!")
            elif self.winner2 is None:
                print("Hand 2 resulted in a push.")

    # def play_again(self):
    #     while self.player.balance > 0 and self.dealer.balance > 0:
    #         self.game_over = str(input("Play again?: "))
    #         if (self.game_over == "Y" or self.game_over == "y" or self.game_over == "yes"
    #                 or self.game_over == "Yes"):
    #             self.game_over = False
    #             self.start()


test = Blackjack()
test.start()
