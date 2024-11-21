import pygame
from Card import Card
from Dealer import Dealer
from Deck import Deck
from Hand import Hand
from Player import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False  # for preventing multiple clicks when only clicking once

    # method will draw the button on the screen and handle getting clicked
    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouse over button and clicked the button
        if self.rect.collidepoint(pos):

            # check if button was clicked (tuple rep. 0 means left click, 1 middle click, 2 right click)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            # make it so that button is clicked once instead of multiple times after 1 click
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        return action

    def blit(self):
        # draw onto screen
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Outline:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class cardObject:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Blackjack:
    def __init__(self, screen):
        self.deck = Deck()
        self.player = Player('Player', 1000)
        self.dealer = Dealer()
        self.bet_amount = 25
        self.game_over = False
        self.hand_count = 1
        self.winner_one = None
        self.winner_two = None
        self.screen = screen
        self.currently_player_turn = True
        self.currently_dealer_turn = False
        self.cards_added_during_player_turn = []
        self.cards_added_during_dealer_turn = []
        self.game_over_card_display = []
        self.pause_iterations_for_game_over = False
        self.split_hand = None
        self.can_split = True
        self.text_font = pygame.font.Font(None, 32)
        self.game_over_text = []

        # initial cards
        self.player_card_1 = None
        self.player_card_2 = None
        self.dealer_card_1 = None
        self.dealer_card_2 = None
        self.dealer_hidden_card = None

        # load button images
        self.hit_img = pygame.image.load('hit.png').convert_alpha()
        self.stand_img = pygame.image.load('stand.png').convert_alpha()
        self.double_img = pygame.image.load('double.png').convert_alpha()
        self.split_img = pygame.image.load('split.png').convert_alpha()
        self.play_again_img = pygame.image.load('playagain.png').convert_alpha()

        # load card extras images
        self.card_back_img = pygame.image.load('Graphics/card extras/card_back.png').convert_alpha()
        self.card_outline = pygame.image.load('Graphics/card extras/card_outline.png').convert_alpha()
        self.cut_card = pygame.image.load('Graphics/card extras/cut_card.png').convert_alpha()

        # load club images
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

        # load diamond images
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

        # load heart images
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

        # load spade images
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

        # create instances
        self.hit_button = Button(83, 500, self.hit_img, 0.75)
        self.stand_button = Button(243, 500, self.stand_img, 0.75)
        self.double_button = Button(403, 500, self.double_img, 0.75)
        self.split_button = Button(563, 500, self.split_img, 0.75)
        self.play_again_button = Button(301, 550, self.play_again_img, 1)

        self.card_outline_table_1 = Outline(95, 250, self.card_outline, 0.75)
        self.card_outline_table_2 = Outline(95, 70, self.card_outline, 0.75)

        # create dictionary for easy image access
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
            },
            "None": {
                "Cut Card": self.cut_card
            }
        }

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, (255, 255, 255))
        screen.blit(img, (x, y))

    def start(self):
        if self.bet_amount <= self.player.balance and self.bet_amount <= self.dealer.balance:
            self.deck.create_deck()
            self.deck.shuffle_deck()
            self.deal()

    # method used to get card images based on card value and suit from dict
    def get_card(self, card):
        return self.card_images[card.suit][card.value]

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

        # Check that card exists, if it does add it to dealer hand and update hand value
        if card2:
            self.dealer.hand.hand.append(card2)

        # Check that card exists, if it does add it to player hand and update hand value
        if card3:
            self.player.hand.hand.append(card3)

        # Check that card exists, if it does add it to dealer hand and update hand value
        if card4:
            self.dealer.hand.hand.append(card4)

        self.player.hand.calc_hand_value()
        self.dealer.hand.calc_hand_value()
        self.player.hand.calc_ability_to_hit()
        self.dealer.hand.calc_ability_to_hit()

        # display starting hands on the screen
        image_for_player_first_card = self.get_card(self.player.hand.hand[0])
        image_for_player_second_card = self.get_card(self.player.hand.hand[1])
        self.player_card_1 = cardObject(108, 305, image_for_player_first_card, 2.5)
        self.player_card_2 = cardObject(178, 305, image_for_player_second_card, 2.5)

        image_for_dealer_first_card = self.get_card(self.dealer.hand.hand[0])
        image_for_dealer_second_card = self.get_card(self.dealer.hand.hand[1])
        self.dealer_card_1 = cardObject(108, 80, image_for_dealer_first_card, 2.5)
        self.dealer_card_2 = cardObject(178, 80, image_for_dealer_second_card, 2.5)
        self.dealer_hidden_card = cardObject(178, 80, self.card_back_img, 2.5)

    def determine_winner(self):

        # hand 1 winner
        if self.hand_count == 1:
            if 21 >= self.player.hand.hand_value > self.dealer.hand.hand_value:
                self.winner_one = self.player
                self.player.balance += self.bet_amount
                self.dealer.balance -= self.bet_amount
            elif 21 >= self.dealer.hand.hand_value > self.player.hand.hand_value:
                self.winner_one = self.dealer
                self.player.balance -= self.bet_amount
                self.dealer.balance += self.bet_amount
            elif self.player.hand.hand_value > 21 >= self.dealer.hand.hand_value:
                self.winner_one = self.dealer
                self.player.balance -= self.bet_amount
                self.dealer.balance += self.bet_amount
            elif self.dealer.hand.hand_value > 21 >= self.player.hand.hand_value:
                self.winner_one = self.player
                self.player.balance += self.bet_amount
                self.dealer.balance -= self.bet_amount
            elif self.player.hand.hand_value == self.dealer.hand.hand_value:
                self.winner_one = None
        else:

            # first hand
            if 21 >= self.player.hand.hand_value > self.dealer.hand.hand_value:
                self.winner_one = self.player
                self.player.balance += self.bet_amount
                self.dealer.balance -= self.bet_amount
            elif 21 >= self.dealer.hand.hand_value > self.player.hand.hand_value:
                self.winner_one = self.dealer
                self.player.balance -= self.bet_amount
                self.dealer.balance += self.bet_amount
            elif self.player.hand.hand_value > 21 >= self.dealer.hand.hand_value:
                self.winner_one = self.dealer
                self.player.balance -= self.bet_amount
                self.dealer.balance += self.bet_amount
            elif self.dealer.hand.hand_value > 21 >= self.player.hand.hand_value:
                self.winner_one = self.player
                self.player.balance += self.bet_amount
                self.dealer.balance -= self.bet_amount
            elif self.player.hand.hand_value == self.dealer.hand.hand_value:
                self.winner_one = None

            # second hand
            if 21 >= self.split_hand.hand_value > self.dealer.hand.hand_value:
                self.winner_two = self.player
                self.player.balance += self.bet_amount
                self.dealer.balance -= self.bet_amount
            elif 21 >= self.dealer.hand.hand_value > self.split_hand.hand_value:
                self.winner_two = self.dealer
                self.player.balance -= self.bet_amount
                self.dealer.balance += self.bet_amount
            elif self.split_hand.hand_value > 21 >= self.dealer.hand.hand_value:
                self.winner_two = self.dealer
                self.player.balance -= self.bet_amount
                self.dealer.balance += self.bet_amount
            elif self.dealer.hand.hand_value > 21 >= self.split_hand.hand_value:
                self.winner_two = self.player
                self.player.balance += self.bet_amount
                self.dealer.balance -= self.bet_amount
            elif self.split_hand.hand_value == self.dealer.hand.hand_value:
                self.winner_two = None

    def play_again(self):
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

        self.currently_player_turn = True
        self.currently_dealer_turn = False
        self.split_hand = None
        self.pause_iterations_for_game_over = False
        self.game_over = False
        self.winner_one = None
        self.winner_two = None

        print(f'hand clear for play again {self.player.hand}')
        print(f'hand clear for play again dealer {self.dealer.hand}')

        self.play_game()

    def play_game(self):
        self.start()

        print(f'player hand after play again {self.player.hand}, hand value {self.player.hand.hand_value}')
        print(f'dealer hand after play again {self.dealer.hand}, hand value {self.dealer.hand.hand_value}')

        run = True
        while run is True:

            # set color of background
            self.screen.fill((53, 101, 77))

            self.hit_button.blit()
            self.stand_button.blit()
            self.double_button.blit()
            self.split_button.blit()
            self.card_outline_table_1.draw()
            self.card_outline_table_2.draw()

            # display initial hands for player and dealer
            self.dealer_card_1.draw()
            self.dealer_hidden_card.draw()
            self.player_card_1.draw()
            self.player_card_2.draw()

            for player_card in self.cards_added_during_player_turn:
                player_card.draw()

            if self.currently_dealer_turn or self.game_over:
                self.dealer_card_2.draw()

            self.cards_added_during_dealer_turn.reverse()
            for dealer_card in self.cards_added_during_dealer_turn:
                dealer_card.draw()

            if self.currently_player_turn:
                if self.player.hand.allowed_to_hit:
                    if self.hit_button.draw():
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
                        self.cards_added_during_player_turn.append(display)
                    elif self.stand_button.draw():
                        self.player.stand()
                    elif self.double_button.draw():
                        self.player.double(self.deck)
                        new_card = self.get_card(self.player.hand.hand[-1])
                        display = cardObject(248, 305, new_card, 2.5)
                        self.cards_added_during_player_turn.append(display)
                    elif self.split_button.draw() and self.can_split:
                        if self.player.hand.hand[0].value == self.player.hand.hand[1].value:
                            self.split_hand = self.player.split(self.deck)
                            self.player.hit(self.deck)

                            # display logic for original player hand
                            new_card = self.get_card(self.player.hand.hand[-1])
                            display = cardObject(178, 305, new_card, 2.5)
                            self.cards_added_during_player_turn.append(display)

                            print(f'{self.split_hand}')
                            # display logic for new hand
                            new_hand_first_card = self.get_card(self.split_hand.hand[0])
                            second_hand_new_card = self.get_card(self.split_hand.hand[-1])
                            display_hand_two_first_card = cardObject(388, 305, new_hand_first_card, 2.5)
                            display_hand_two = cardObject(458, 305, second_hand_new_card, 2.5)
                            self.cards_added_during_player_turn.append(display_hand_two_first_card)
                            self.cards_added_during_player_turn.append(display_hand_two)
                            self.can_split = False
                            self.split_hand.allowed_to_hit = True
                            self.hand_count += 1

                if self.split_hand is not None:
                    if self.split_hand.allowed_to_hit is True:
                        if self.hit_button.draw():
                            self.split_hand.hit(self.deck)
                            new_card = self.get_card(self.split_hand.hand[-1])
                            if len(self.split_hand.hand) == 3:
                                display = cardObject(528, 305, new_card, 2.5)
                            self.cards_added_during_player_turn.append(display)
                        elif self.stand_button.draw():
                            self.split_hand.stand()
                        elif self.double_button.draw():
                            self.split_hand.double(self.deck)
                            new_card = self.get_card(self.split_hand.hand[-1])
                            display = cardObject(528, 305, new_card, 2.5)
                            self.cards_added_during_player_turn.append(display)

            if self.split_hand is None:
                if (self.currently_player_turn and not self.player.hand.allowed_to_hit
                        and not self.pause_iterations_for_game_over):
                    self.currently_player_turn = False
                    self.currently_dealer_turn = True
            elif self.split_hand is not None:
                if (self.currently_player_turn and not self.player.hand.allowed_to_hit
                        and self.split_hand.allowed_to_split and not
                        self.pause_iterations_for_game_over):
                    self.currently_player_turn = True
                    self.currently_dealer_turn = False
                elif (self.currently_player_turn and not self.player.hand.allowed_to_hit
                        and not self.split_hand.allowed_to_hit and not
                        self.pause_iterations_for_game_over):
                    self.currently_player_turn = False
                    self.currently_dealer_turn = True

            if self.currently_dealer_turn:
                if self.dealer.hand.allowed_to_hit:
                    self.dealer.play(self.deck)

                    # update display of card 2 in player hand
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
                    self.cards_added_during_dealer_turn.append(display)

            # reverse dealer cards back from previous reverse so it is in correct added order
            self.cards_added_during_dealer_turn.reverse()

            if self.dealer.hand.allowed_to_hit is False:
                if self.currently_dealer_turn is True:
                    self.currently_dealer_turn = False
                    self.game_over = True
                    self.pause_iterations_for_game_over = True

            if self.game_over:
                self.determine_winner()
                if self.hand_count == 1:
                    if self.winner_one == self.player:
                        self.draw_text("Player Wins!", self.text_font, (0, 0, 0), 335, 263)
                    elif self.winner_one == self.dealer:
                        self.draw_text("Dealer Wins!", self.text_font, (0, 0, 0), 335, 263)
                    else:
                        self.draw_text("Push!", self.text_font, (0, 0, 0), 370, 263)
                else:
                    if self.winner_one == self.player and self.winner_two == self.player:
                        self.draw_text("Player Wins Both Hands!", self.text_font, (0, 0, 0), 335, 263)
                    elif self.winner_one == self.dealer and self.winner_two == self.dealer:
                        self.draw_text("Dealer Wins Both Hands!", self.text_font, (0, 0, 0), 335, 263)
                    elif self.winner_one == self.player and self.winner_two == self.dealer:
                        self.draw_text("Player Wins Hand 1, Dealer Wins Hand 2!", self.text_font, (0, 0, 0), 370, 263)
                    elif self.winner_one == self.dealer and self.winner_two == self.player:
                        self.draw_text("Dealer Wins Hand 1, Player Wins Hand 2!", self.text_font, (0, 0, 0), 370, 263)
                    elif self.winner_one == self.player and self.winner_two == None:
                        self.draw_text("Player Wins Hand 1, Push Hand 2!", self.text_font, (0, 0, 0), 370, 263)
                    elif self.winner_one == self.dealer and self.winner_two == None:
                        self.draw_text("Dealer Wins Hand 1, Push Hand 2!", self.text_font, (0, 0, 0), 370, 263)
                    elif self.winner_one == None and self.winner_two == self.player:
                        self.draw_text("Push Hand 1, Player Wins Hand 2!", self.text_font, (0, 0, 0), 370, 263)
                    elif self.winner_one == None and self.winner_two == self.dealer:
                        self.draw_text("Push Hand 1, Dealer Wins Hand 2!", self.text_font, (0, 0, 0), 370, 263)
                    else:
                        self.draw_text("Push Both Hands", self.text_font, (0, 0, 0), 370, 263)

            # display hand values on the screen
            if self.split_hand is None:
                self.draw_text(f'{self.player.hand.hand_value}', self.text_font, (0, 0, 0), 110, 263)
            else:
                self.draw_text(f'{self.player.hand.hand_value}', self.text_font, (0, 0, 0), 110, 263)
                self.draw_text(f'{self.split_hand.hand_value}', self.text_font, (0, 0, 0), 70, 263)

            if len(self.dealer.hand.hand) == 2:
                value = 0
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

            if self.game_over:
                self.play_again_button.blit()
                if self.play_again_button.draw():
                    print(" ")
                    print(" ")
                    print(" ")
                    print("--------------------------------------------------------")
                    print("--------------------------------------------------------")
                    print("--------------------- PLAY AGAIN -----------------------")
                    print("--------------------------------------------------------")
                    print("--------------------------------------------------------")
                    print(" ")
                    print(" ")
                    print(" ")
                    run = False
                    self.play_again()

            pygame.display.update()

            """ EVENT HANDLER """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


test = Blackjack(screen)
test.play_game()
pygame.quit()
