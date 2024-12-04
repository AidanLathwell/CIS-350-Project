import pygame
from Card import Card
from Dealer import Dealer
from Deck import Deck
from Hand import Hand
from Player import Player


pygame.init()
screen = pygame.display.set_mode((800, 600))

""" Button class that wil create button objects to display on the screen. """
class Button:

    
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False  # for preventing multiple clicks when only clicking once

    """ Method will determine if a button gets clicked. """
    def draw(self):
        action = False

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse over button and clicked the button
        if self.rect.collidepoint(pos):

            # Check if button was clicked (tuple rep. 0 means left click, 1 middle click, 2 right click)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            # Make it so that button is clicked once instead of multiple times after 1 click
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        return action

    """ Method that will draw the button on to the screen. """
    def blit(self):

        # Draw onto screen
        screen.blit(self.image, (self.rect.x, self.rect.y))


""" Outline class that will create the outline of the blackjack table on the screen. """
class Outline:

    
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    """ Method that will draw the outlines on to the screen. """
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

""" Card object class which transforms card png images into drawable objects. """
class cardObject:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    """ Method that will draw the cards on to the screen. """
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


""" Blackjack class that will run the gui and all game logic. """
class Blackjack:

    
    def __init__(self, screen):

        # Instance Variables
        self.deck = Deck()
        self.player = Player('Player', 1000)
        self.dealer = Dealer()
        self.bet_amount = 25
        self.game_over = False
        self.winner = None
        self.screen = screen
        self.currently_player_turn = True
        self.currently_dealer_turn = False
        self.cards_added_during_player_turn = []
        self.cards_added_during_dealer_turn = []
        self.game_over_card_display = []
        self.pause_iterations_for_game_over = False
        self.text_font = pygame.font.Font(None, 32)
        self.game_over_text = []
        self.number_of_bets_subtracted = 0
        self.bet_message_display = "Bet Amount (change before hitting):"
        self.user_text = ""

        # Initial cards, only used for the beginning of the games display
        self.player_card_1 = None
        self.player_card_2 = None
        self.dealer_card_1 = None
        self.dealer_card_2 = None
        self.dealer_hidden_card = None

        # Load button images
        self.hit_img = pygame.image.load('hit.png').convert_alpha()
        self.stand_img = pygame.image.load('stand.png').convert_alpha()
        self.double_img = pygame.image.load('double.png').convert_alpha()
        self.play_again_img = pygame.image.load('playagain.png').convert_alpha()

        # Load card extras images
        self.card_back_img = pygame.image.load('Graphics/card extras/card_back.png').convert_alpha()
        self.card_outline = pygame.image.load('Graphics/card extras/card_outline.png').convert_alpha()

        # Load images for each suit and value
        self.club_card_2 = pygame.image.load('Graphics/clubs/card_clubs_02.png').convert_alpha()
        self.club_card_3 = pygame.image.load('Graphics/clubs/card_clubs_03.png').convert_alpha()
        self.club_card_4 = pygame.image.load('Graphics/clubs/card_clubs_04.png').convert_alpha()
        self.club_card_5 = pygame.image.load('Graphics/clubs/card_clubs_05.png').convert_alpha()
        self.club_card_6 = pygame.image.load('Graphics/clubs/card_clubs_06.png').convert_alpha()
        self.club_card_7 = pygame.image.load('Graphics/clubs/card_clubs_07.png').convert_alpha()
        self.club_card_8 = pygame.image.load('Graphics/clubs/card_clubs_08.png').convert_alpha()
        self.club_card_9 = pygame.image.load('Graphics/clubs/card_clubs_09.png').convert_alpha()
        self.club_card_10 = pygame.image.load('Graphics/clubs/card_clubs_10.png').convert_alpha()
        self.club_card_A = pygame.image.load('Graphics/clubs/card_clubs_A.png').convert_alpha()
        self.club_card_J = pygame.image.load('Graphics/clubs/card_clubs_J.png').convert_alpha()
        self.club_card_Q = pygame.image.load('Graphics/clubs/card_clubs_Q.png').convert_alpha()
        self.club_card_K = pygame.image.load('Graphics/clubs/card_clubs_K.png').convert_alpha()
        self.diamond_card_2 = pygame.image.load('Graphics/diamonds/card_diamonds_02.png').convert_alpha()
        self.diamond_card_3 = pygame.image.load('Graphics/diamonds/card_diamonds_03.png').convert_alpha()
        self.diamond_card_4 = pygame.image.load('Graphics/diamonds/card_diamonds_04.png').convert_alpha()
        self.diamond_card_5 = pygame.image.load('Graphics/diamonds/card_diamonds_05.png').convert_alpha()
        self.diamond_card_6 = pygame.image.load('Graphics/diamonds/card_diamonds_06.png').convert_alpha()
        self.diamond_card_7 = pygame.image.load('Graphics/diamonds/card_diamonds_07.png').convert_alpha()
        self.diamond_card_8 = pygame.image.load('Graphics/diamonds/card_diamonds_08.png').convert_alpha()
        self.diamond_card_9 = pygame.image.load('Graphics/diamonds/card_diamonds_09.png').convert_alpha()
        self.diamond_card_10 = pygame.image.load('Graphics/diamonds/card_diamonds_10.png').convert_alpha()
        self.diamond_card_A = pygame.image.load('Graphics/diamonds/card_diamonds_A.png').convert_alpha()
        self.diamond_card_J = pygame.image.load('Graphics/diamonds/card_diamonds_J.png').convert_alpha()
        self.diamond_card_Q = pygame.image.load('Graphics/diamonds/card_diamonds_Q.png').convert_alpha()
        self.diamond_card_K = pygame.image.load('Graphics/diamonds/card_diamonds_K.png').convert_alpha()
        self.hearts_card_2 = pygame.image.load('Graphics/hearts/card_hearts_02.png').convert_alpha()
        self.hearts_card_3 = pygame.image.load('Graphics/hearts/card_hearts_03.png').convert_alpha()
        self.hearts_card_4 = pygame.image.load('Graphics/hearts/card_hearts_04.png').convert_alpha()
        self.hearts_card_5 = pygame.image.load('Graphics/hearts/card_hearts_05.png').convert_alpha()
        self.hearts_card_6 = pygame.image.load('Graphics/hearts/card_hearts_06.png').convert_alpha()
        self.hearts_card_7 = pygame.image.load('Graphics/hearts/card_hearts_07.png').convert_alpha()
        self.hearts_card_8 = pygame.image.load('Graphics/hearts/card_hearts_08.png').convert_alpha()
        self.hearts_card_9 = pygame.image.load('Graphics/hearts/card_hearts_09.png').convert_alpha()
        self.hearts_card_10 = pygame.image.load('Graphics/hearts/card_hearts_10.png').convert_alpha()
        self.hearts_card_A = pygame.image.load('Graphics/hearts/card_hearts_A.png').convert_alpha()
        self.hearts_card_J = pygame.image.load('Graphics/hearts/card_hearts_J.png').convert_alpha()
        self.hearts_card_Q = pygame.image.load('Graphics/hearts/card_hearts_Q.png').convert_alpha()
        self.hearts_card_K = pygame.image.load('Graphics/hearts/card_hearts_K.png').convert_alpha()
        self.spades_card_2 = pygame.image.load('Graphics/spades/card_spades_02.png').convert_alpha()
        self.spades_card_3 = pygame.image.load('Graphics/spades/card_spades_03.png').convert_alpha()
        self.spades_card_4 = pygame.image.load('Graphics/spades/card_spades_04.png').convert_alpha()
        self.spades_card_5 = pygame.image.load('Graphics/spades/card_spades_05.png').convert_alpha()
        self.spades_card_6 = pygame.image.load('Graphics/spades/card_spades_06.png').convert_alpha()
        self.spades_card_7 = pygame.image.load('Graphics/spades/card_spades_07.png').convert_alpha()
        self.spades_card_8 = pygame.image.load('Graphics/spades/card_spades_08.png').convert_alpha()
        self.spades_card_9 = pygame.image.load('Graphics/spades/card_spades_09.png').convert_alpha()
        self.spades_card_10 = pygame.image.load('Graphics/spades/card_spades_10.png').convert_alpha()
        self.spades_card_A = pygame.image.load('Graphics/spades/card_spades_A.png').convert_alpha()
        self.spades_card_J = pygame.image.load('Graphics/spades/card_spades_J.png').convert_alpha()
        self.spades_card_Q = pygame.image.load('Graphics/spades/card_spades_Q.png').convert_alpha()
        self.spades_card_K = pygame.image.load('Graphics/spades/card_spades_K.png').convert_alpha()

        # Create button objects
        self.hit_button = Button(160, 500, self.hit_img, 0.75)
        self.stand_button = Button(320, 500, self.stand_img, 0.75)
        self.double_button = Button(480, 500, self.double_img, 0.75)
        self.play_again_button = Button(298, 550, self.play_again_img, 1)

        # Create table outline objects
        self.card_outline_table_1 = Outline(95, 250, self.card_outline, 0.75)
        self.card_outline_table_2 = Outline(95, 70, self.card_outline, 0.75)

        # Dictionary for easy image access
        self.card_images = {
            "Clubs": {
                "Ace": self.club_card_A,
                "2": self.club_card_2,
                "3": self.club_card_3,
                "4": self.club_card_4,
                "5": self.club_card_5,
                "6": self.club_card_6,
                "7": self.club_card_7,
                "8": self.club_card_8,
                "9": self.club_card_9,
                "10": self.club_card_10,
                "Jack": self.club_card_J,
                "Queen": self.club_card_Q,
                "King": self.club_card_K
            },
            "Diamonds": {
                "Ace": self.diamond_card_A,
                "2": self.diamond_card_2,
                "3": self.diamond_card_3,
                "4": self.diamond_card_4,
                "5": self.diamond_card_5,
                "6": self.diamond_card_6,
                "7": self.diamond_card_7,
                "8": self.diamond_card_8,
                "9": self.diamond_card_9,
                "10": self.diamond_card_10,
                "Jack": self.diamond_card_J,
                "Queen": self.diamond_card_Q,
                "King": self.diamond_card_K
            },
            "Hearts": {
                "Ace": self.hearts_card_A,
                "2": self.hearts_card_2,
                "3": self.hearts_card_3,
                "4": self.hearts_card_4,
                "5": self.hearts_card_5,
                "6": self.hearts_card_6,
                "7": self.hearts_card_7,
                "8": self.hearts_card_8,
                "9": self.hearts_card_9,
                "10": self.hearts_card_10,
                "Jack": self.hearts_card_J,
                "Queen": self.hearts_card_Q,
                "King": self.hearts_card_K
            },
            "Spades": {
                "Ace": self.spades_card_A,
                "2": self.spades_card_2,
                "3": self.spades_card_3,
                "4": self.spades_card_4,
                "5": self.spades_card_5,
                "6": self.spades_card_6,
                "7": self.spades_card_7,
                "8": self.spades_card_8,
                "9": self.spades_card_9,
                "10": self.spades_card_10,
                "Jack": self.spades_card_J,
                "Queen": self.spades_card_Q,
                "King": self.spades_card_K
            }
        }

    """ Method called to display game result text on screen after the game ends. """
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, (255, 255, 255))
        screen.blit(img, (x, y))

    """ Method called to start the game. It will create and randomize the deck, then
        call for the deal method. """
    def start(self):

        # Ensure player and dealer have enough money to bet, then create deck and call deal
        if self.bet_amount <= self.player.balance and self.bet_amount <= self.dealer.balance:
            self.deck.create_deck()
            self.deck.shuffle_deck()
            self.deal()

    """ Method used to get card images based on card value and suit from the dictionary. """
    def get_card(self, card):
        return self.card_images[card.suit][card.value]

    """ Method will hit and intial two cards for dealer and player hands. It will then
        calculate the ability for the dealer and player to be able to hit, as well as
        their hand values. """
    def deal(self):

        # Draw initial player and dealer cards from the deck
        card1 = self.deck.hit()
        card2 = self.deck.hit()
        card3 = self.deck.hit()
        card4 = self.deck.hit()

        # Add cards to player respective hands
        self.player.hand.hand.append(card1)
        self.dealer.hand.hand.append(card2)
        self.player.hand.hand.append(card3)
        self.dealer.hand.hand.append(card4)

        # Calculate player respective hand value and ability to hit
        self.player.hand.calc_hand_value()
        self.dealer.hand.calc_hand_value()
        self.player.hand.calc_ability_to_hit()
        self.dealer.hand.calc_ability_to_hit()

        # Display starting hand on the screen for the player
        image_for_player_first_card = self.get_card(self.player.hand.hand[0])
        image_for_player_second_card = self.get_card(self.player.hand.hand[1])
        self.player_card_1 = cardObject(108, 305, image_for_player_first_card, 2.5)
        self.player_card_2 = cardObject(178, 305, image_for_player_second_card, 2.5)

        """ Display starting hand on screen for dealer. Will initially display a
            backwards card for the dealers second card to hide it. The real second
            card is still assigned to the correct variable for later display. """
        image_for_dealer_first_card = self.get_card(self.dealer.hand.hand[0])
        image_for_dealer_second_card = self.get_card(self.dealer.hand.hand[1])
        self.dealer_card_1 = cardObject(108, 80, image_for_dealer_first_card, 2.5)
        self.dealer_card_2 = cardObject(178, 80, image_for_dealer_second_card, 2.5)
        self.dealer_hidden_card = cardObject(178, 80, self.card_back_img, 2.5)

    """ Method called after the game ends to determine the winner. """
    def determine_winner(self):

        if self.game_over and self.number_of_bets_subtracted == 0:
            self.number_of_bets_subtracted += 1
            # Check which case applies to the game state and assign results
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

    """ Method called to restart the game. This method can only be called after the
        game is over. It will set the game variables back to their original state 
        and then call the play game method to start another game. """
    def play_again(self):

        # Clear all variables stored in respective lists
        while len(self.player.hand.hand) > 0:
            self.player.hand.hand.pop(-1)
        while len(self.dealer.hand.hand) > 0:
            self.dealer.hand.hand.pop(-1)
        while len(self.cards_added_during_player_turn) > 0:
            self.cards_added_during_player_turn.pop(-1)
        while len(self.cards_added_during_dealer_turn) > 0:
            self.cards_added_during_dealer_turn.pop(-1)
        while len(self.game_over_card_display) > 0:
            self.game_over_card_display.pop(-1)

        # Set all variables back to original game state prior to start
        self.currently_player_turn = True
        self.player.hand.already_hit = False
        self.currently_dealer_turn = False
        self.pause_iterations_for_game_over = False
        self.game_over = False
        self.winner = None
        self.number_of_bets_subtracted = 0

        # Call play game method to start another game
        self.play_game()

    """ Method that handles the GUI display. It will have a while loop run non stop until
        the play again method is called. It will actively display new cards and status
        game information like hand value, winner, and more while running. """
    def play_game(self):

        # Call start method to create deck and deal initial hands
        self.start()

        # Variable to start and end while loop
        run = True

        # Game loop, it will run until the play again method is called
        while run is True:

            # Set color of background
            self.screen.fill((53, 101, 77))

            # Display buttons and table outline on the screen
            self.hit_button.blit()
            self.stand_button.blit()
            self.double_button.blit()
            self.card_outline_table_1.draw()
            self.card_outline_table_2.draw()

            # Display initial cards for player and dealer
            self.dealer_card_1.draw()
            self.player_card_1.draw()
            self.player_card_2.draw()

            """ This if statement will handle drawing the dealers second card. When
                applicable, it will draw the desired card"""
            if self.currently_dealer_turn or self.game_over:
                self.dealer_card_2.draw()
            else:
               self.dealer_hidden_card.draw()

            """ This for loop will draw the players cards onto the screen. Because
                this is a never ending while loop, the cards need to be redrawn
                every iteration. """
            for player_card in self.cards_added_during_player_turn:
                player_card.draw()

            """ Used to undo the reversing of the dealers cards after each iteration. 
                When you hit, you add to the end of a list. This will ensure cards
                are drawn in the correct order. """
            self.cards_added_during_dealer_turn.reverse()

            """ This for loop will draw the dealers cards onto the screen. Because
                this is a never ending while loop, the cards need to be redrawn
                every iteration. """
            for dealer_card in self.cards_added_during_dealer_turn:
                dealer_card.draw()

            # Portion of code that will handle the players turn
            if self.currently_player_turn:
                if self.player.hand.allowed_to_hit:

                    # Check if the hit button was clicked
                    if self.hit_button.draw():

                        # Get the new card and set its display location
                        self.player.hit(self.deck)
                        new_card = self.get_card(self.player.hand.hand[-1])
                        if len(self.player.hand.hand) == 3:
                            display = cardObject(248, 305, new_card, 2.5)
                        elif len(self.player.hand.hand) == 4:
                            display = cardObject(318, 305, new_card, 2.5)
                        elif len(self.player.hand.hand) == 5:
                            display = cardObject(388, 305, new_card, 2.5)
                        elif len(self.player.hand.hand) == 6:
                            display = cardObject(458, 305, new_card, 2.5)
                        else:
                            display = cardObject(528, 305, new_card, 2.5)

                        """ Add display card to players turn list. This is so
                            that the card displays during all iterations. """
                        self.cards_added_during_player_turn.append(display)

                    # Check if the stand button was clicked
                    elif self.stand_button.draw():

                        # Set ability to hit to false and allow dealer to play
                        self.player.stand()

                    # Check if the double button was clicked
                    elif self.double_button.draw():

                        # Get new player card and set its display location
                        self.player.double(self.deck)
                        new_card = self.get_card(self.player.hand.hand[-1])
                        display = cardObject(248, 305, new_card, 2.5)
                        self.cards_added_during_player_turn.append(display)

            """ This if statement will change the current player to the dealer when
                a player can no longer play and the game is not over. """
            if (self.currently_player_turn and not self.player.hand.allowed_to_hit
                    and not self.pause_iterations_for_game_over):
                self.currently_player_turn = False
                self.currently_dealer_turn = True

            # Portion of code that will handle the dealers turn
            if self.currently_dealer_turn:
                if self.dealer.hand.allowed_to_hit:

                    # Get the new card and set its display location
                    self.dealer.play(self.deck)
                    new_card = self.get_card(self.dealer.hand.hand[-1])
                    if len(self.dealer.hand.hand) == 3:
                        display = cardObject(248, 80, new_card, 2.5)
                    elif len(self.dealer.hand.hand) == 4:
                        display = cardObject(318, 80, new_card, 2.5)
                    elif len(self.dealer.hand.hand) == 5:
                        display = cardObject(388, 80, new_card, 2.5)
                    elif len(self.dealer.hand.hand) == 6:
                        display = cardObject(458, 80, new_card, 2.5)
                    else:
                        display = cardObject(528, 80, new_card, 2.5)

                    """ Add display card to dealers turn list. This is so
                        that the card displays during all iterations. """
                    self.cards_added_during_dealer_turn.append(display)

            """ This if statement will change the the dealers hand to false, game over
                to true, and pause game for iterations to true. This is because the
                dealer has completed its turn so now the game over logic will be called.
                By setting pause for iterations to true, we are ensuring display stays
                the same. """
            if self.dealer.hand.allowed_to_hit is False:
                if self.currently_dealer_turn is True:
                    self.currently_dealer_turn = False
                    self.game_over = True
                    self.pause_iterations_for_game_over = True

            # Display player hand value on the screen
            self.draw_text(f'{self.player.hand.hand_value}', self.text_font, (0, 0, 0), 110, 263)

            # Display dealer hand value on the screen
            if len(self.dealer.hand.hand) == 2:
                if (self.dealer.hand.hand[0].value == "Jack" or self.dealer.hand.hand[0].value == "Queen"
                        or self.dealer.hand.hand[0].value == "King"):
                    value = 10
                elif self.dealer.hand.hand[0].value == "Ace":
                    value = 11
                else:
                    value = self.dealer.hand.hand[0].value
                self.draw_text(f'{value}', self.text_font, (0, 0, 0), 660, 263)
            else:
                self.draw_text(f'{self.dealer.hand.hand_value}', self.text_font, (0, 0, 0), 660, 263)

            """ Reverse the order of the dealers cards in hand. This will ensure cards
                are drawn in the correct order. """
            self.cards_added_during_dealer_turn.reverse()

            # If statement that will assign the display text based on the game results
            if self.game_over:

                # Method called to determine winner
                self.determine_winner()
                if self.winner == self.player:
                    self.draw_text("Player Wins!", self.text_font, (0, 0, 0), 335, 263)
                elif self.winner == self.dealer:
                    self.draw_text("Dealer Wins!", self.text_font, (0, 0, 0), 335, 263)
                else:
                    self.draw_text("Push!", self.text_font, (0, 0, 0), 370, 263)

                # Draw play again button onto the screen
                self.play_again_button.blit()

                # Check if play again button is clicked
                if self.play_again_button.draw():

                    # Temporary stop the loop and call the play again method
                    run = False
                    self.play_again()

            """ EVENT HANDLER """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if self.player.hand.already_hit is False:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text = self.user_text[:-1]
                        else:
                            self.user_text += event.unicode
                            self.bet_amount = int(self.user_text)

            # display original bet amount if no new bet
            if self.user_text == "":
                self.draw_text("25", self.text_font, (255, 255, 255), 565, 40)
                self.bet_amount = 25
            else:

                # display bet amount message and value
                self.draw_text(self.user_text, self.text_font, (255, 255, 255), 565, 40)
            self.draw_text("Bet Amount (change before hitting) :", self.text_font, (255, 255, 255), 170, 40)

            # Display player and dealer balances
            self.draw_text("Player Balance:", self.text_font, (255, 255, 255), 10, 560)
            self.draw_text(f'{self.player.balance}', self.text_font, (255, 255, 255), 180, 560)
            self.draw_text("Dealer Balance:", self.text_font, (255, 255, 255), 550, 560)
            self.draw_text(f'{self.dealer.balance}', self.text_font, (255, 255, 255), 722, 560)

            # Update screen display after each iteration
            pygame.display.update()


test = Blackjack(screen)
test.play_game()
pygame.quit()
