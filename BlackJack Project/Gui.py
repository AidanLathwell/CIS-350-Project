import pygame
from Card import Card
from Dealer import Dealer
from Card import Card
from Hand import Hand
from Player import Player

pygame.init()

""" CREATE WINDOW """
# create the window with the input dimensions
screen = pygame.display.set_mode((800, 600))

# load button images
hit_img = pygame.image.load('hit.png').convert_alpha()
stand_img = pygame.image.load('stand.png').convert_alpha()
double_img = pygame.image.load('double.png').convert_alpha()
split_img = pygame.image.load('split.png').convert_alpha()

# load card extras images
card_back_img = pygame.image.load('Graphics/card extras/card_back.png').convert_alpha()
card_outline = pygame.image.load('Graphics/card extras/card_outline.png').convert_alpha()

# load club images
club_card_2 = pygame.image.load('Graphics/clubs/card_clubs_02.png').convert_alpha()
club_card_3 = pygame.image.load('Graphics/clubs/card_clubs_03.png').convert_alpha()
club_card_4 = pygame.image.load('Graphics/clubs/card_clubs_04.png').convert_alpha()
club_card_5 = pygame.image.load('Graphics/clubs/card_clubs_05.png').convert_alpha()
club_card_6 = pygame.image.load('Graphics/clubs/card_clubs_06.png').convert_alpha()
club_card_7 = pygame.image.load('Graphics/clubs/card_clubs_07.png').convert_alpha()
club_card_8 = pygame.image.load('Graphics/clubs/card_clubs_08.png').convert_alpha()
club_card_9 = pygame.image.load('Graphics/clubs/card_clubs_09.png').convert_alpha()
club_card_10 = pygame.image.load('Graphics/clubs/card_clubs_10.png').convert_alpha()
club_card_A = pygame.image.load('Graphics/clubs/card_clubs_A.png').convert_alpha()
club_card_J = pygame.image.load('Graphics/clubs/card_clubs_J.png').convert_alpha()
club_card_Q = pygame.image.load('Graphics/clubs/card_clubs_K.png').convert_alpha()
club_card_K = pygame.image.load('Graphics/clubs/card_clubs_Q.png').convert_alpha()

# load diamond images
diamond_card_1 = pygame.image.load('Graphics/diamonds/card_diamonds_02.png').convert_alpha()
diamond_card_3 = pygame.image.load('Graphics/diamonds/card_diamonds_03.png').convert_alpha()
diamond_card_4 = pygame.image.load('Graphics/diamonds/card_diamonds_04.png').convert_alpha()
diamond_card_5 = pygame.image.load('Graphics/diamonds/card_diamonds_05.png').convert_alpha()
diamond_card_6 = pygame.image.load('Graphics/diamonds/card_diamonds_06.png').convert_alpha()
diamond_card_7 = pygame.image.load('Graphics/diamonds/card_diamonds_07.png').convert_alpha()
diamond_card_8 = pygame.image.load('Graphics/diamonds/card_diamonds_08.png').convert_alpha()
diamond_card_9 = pygame.image.load('Graphics/diamonds/card_diamonds_09.png').convert_alpha()
diamond_card_10 = pygame.image.load('Graphics/diamonds/card_diamonds_10.png').convert_alpha()
diamond_card_A = pygame.image.load('Graphics/diamonds/card_diamonds_A.png').convert_alpha()
diamond_card_J = pygame.image.load('Graphics/diamonds/card_diamonds_J.png').convert_alpha()
diamond_card_Q = pygame.image.load('Graphics/diamonds/card_diamonds_K.png').convert_alpha()
diamond_card_K = pygame.image.load('Graphics/diamonds/card_diamonds_Q.png').convert_alpha()

# load heart images
hearts_card_1 = pygame.image.load('Graphics/hearts/card_hearts_02.png').convert_alpha()
hearts_card_3 = pygame.image.load('Graphics/hearts/card_hearts_03.png').convert_alpha()
hearts_card_4 = pygame.image.load('Graphics/hearts/card_hearts_04.png').convert_alpha()
hearts_card_5 = pygame.image.load('Graphics/hearts/card_hearts_05.png').convert_alpha()
hearts_card_6 = pygame.image.load('Graphics/hearts/card_hearts_06.png').convert_alpha()
hearts_card_7 = pygame.image.load('Graphics/hearts/card_hearts_07.png').convert_alpha()
hearts_card_8 = pygame.image.load('Graphics/hearts/card_hearts_08.png').convert_alpha()
hearts_card_9 = pygame.image.load('Graphics/hearts/card_hearts_09.png').convert_alpha()
hearts_card_10 = pygame.image.load('Graphics/hearts/card_hearts_10.png').convert_alpha()
hearts_card_A = pygame.image.load('Graphics/hearts/card_hearts_A.png').convert_alpha()
hearts_card_J = pygame.image.load('Graphics/hearts/card_hearts_J.png').convert_alpha()
hearts_card_Q = pygame.image.load('Graphics/hearts/card_hearts_K.png').convert_alpha()
hearts_card_K = pygame.image.load('Graphics/hearts/card_hearts_Q.png').convert_alpha()

# load spade images
spades_card_1 = pygame.image.load('Graphics/spades/card_spades_02.png').convert_alpha()
spades_card_3 = pygame.image.load('Graphics/spades/card_spades_03.png').convert_alpha()
spades_card_4 = pygame.image.load('Graphics/spades/card_spades_04.png').convert_alpha()
spades_card_5 = pygame.image.load('Graphics/spades/card_spades_05.png').convert_alpha()
spades_card_6 = pygame.image.load('Graphics/spades/card_spades_06.png').convert_alpha()
spades_card_7 = pygame.image.load('Graphics/spades/card_spades_07.png').convert_alpha()
spades_card_8 = pygame.image.load('Graphics/spades/card_spades_08.png').convert_alpha()
spades_card_9 = pygame.image.load('Graphics/spades/card_spades_09.png').convert_alpha()
spades_card_10 = pygame.image.load('Graphics/spades/card_spades_10.png').convert_alpha()
spades_card_A = pygame.image.load('Graphics/spades/card_spades_A.png').convert_alpha()
spades_card_J = pygame.image.load('Graphics/spades/card_spades_J.png').convert_alpha()
spades_card_Q = pygame.image.load('Graphics/spades/card_spades_K.png').convert_alpha()
spades_card_K = pygame.image.load('Graphics/spades/card_spades_Q.png').convert_alpha()

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

        # draw onto screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

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

# create instances
hit_button = Button(83, 500, hit_img, 0.75)
stand_button = Button(243, 500, stand_img, 0.75)
double_button = Button(403, 500, double_img, 0.75)
split_button = Button(563, 500, split_img, 0.75)

card_outline_table_1 = Outline(95, 250, card_outline, 0.75)
card_outline_table_2 = Outline(95, 70, card_outline, 0.75)

# CARD PLACEMENTS FOR PLAYER HANDS
# test_card = cardObject(108, 305, club_card_2, 2.5)
# test_card_2 = cardObject(178, 305, club_card_2, 2.5)
# test_card_3 = cardObject(248, 305, club_card_2, 2.5)
# test_card_4 = cardObject(318, 305, club_card_2, 2.5)
# test_card_5 = cardObject(388, 305, club_card_2, 2.5)
# test_card_6 = cardObject(458, 305, club_card_2, 2.5)
# test_card_7 = cardObject(528, 305, club_card_2, 2.5)

# CARD PLACEMENTS FOR DEALER HANDS
# test_card = cardObject(108, 80, club_card_2, 2.5)
# test_card_2 = cardObject(178, 80, club_card_2, 2.5)
# test_card_3 = cardObject(248, 80, club_card_2, 2.5)
# test_card_4 = cardObject(318, 80, club_card_2, 2.5)
# test_card_5 = cardObject(388, 80, club_card_2, 2.5)
# test_card_6 = cardObject(458, 80, club_card_2, 2.5)
# test_card_7 = cardObject(528, 80, club_card_2, 2.5)

run = True
while run is True:

    # set color of backround
    screen.fill((53, 101, 77))

    card_outline_table_1.draw()
    card_outline_table_2.draw()

    if hit_button.draw():
        print("HIT")
    elif stand_button.draw():
        print('STAND')
    elif double_button.draw():
        print('DOUBLE')
    elif split_button.draw():
        print('SPLIT')

    """ EVENT HANDLER """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()