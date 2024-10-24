import pygame

pygame.init()

""" CREATE WINDOW """
# variables to assign the screen size dimensions
screen_width = 800
screen_height = 600

# create the window with the input dimensions
screen = pygame.display.set_mode((screen_width, screen_height))

# load button images
hit_img = pygame.image.load('hit.png').convert_alpha()
stand_img = pygame.image.load('stand.png').convert_alpha()
double_img = pygame.image.load('double.png').convert_alpha()
split_img = pygame.image.load('split.png').convert_alpha()

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False # for preventing multiple clicks when only clicking once

    # method will draw the button on the screen
    def draw(self):
        action = False

        # get mouse postion
        pos = pygame.mouse.get_pos()

        # check mouse over button and clicked the button
        if self.rect.collidepoint(pos):

            # check if button was clicked (tuple rep. 0 means left click)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

hit_button = Button(83, 500, hit_img, 0.75)
stand_button = Button(243, 500, stand_img, 0.75)
double_button = Button(403, 500, double_img, 0.75)
split_button = Button(563, 500, split_img, 0.75)

""" CREATE GAME LOOP """
run = True
while run is True:

    # set color of backround
    screen.fill((53, 101, 77))

    if hit_button.draw():
        print('HIT')
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


