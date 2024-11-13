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
        self.clicked = False # for preventing multiple clicks when only clicking once

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
        self.screen = screen

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

    def play_game(self):
        self.start()
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

            pygame.display.update()

            while self.player.hand.allowed_to_hit:
                if self.hit_button.draw():
                    self.player.hit(self.deck)
                    new_card = self.get_card(self.player.hand.hand[-1])
                    display = cardObject(248, 305, new_card, 2.5)
                    display.draw()
                    print(self.player.hand)
                    print("HIT")
                elif self.stand_button.draw():
                    self.player.stand()
                    print(self.player.hand)
                    print('STAND')
                elif self.double_button.draw():
                    self.player.double(self.deck)
                    print(self.player.hand)
                    print('DOUBLE')
                elif self.split_button.draw():
                    new_hand = self.player.split(self.deck)
                    self.player.hit(self.deck)
                    print(self.player.hand)
                    print(new_hand)
                    print('SPLIT')
                pygame.display.update()

            pygame.display.update()

            """ EVENT HANDLER """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


test = Blackjack(screen)
test.play_game()
pygame.quit()
