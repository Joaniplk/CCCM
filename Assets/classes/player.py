import os
import pygame
import classes.controls as controls

class Player:
    def __init__(self, width, height, vel, image_uri, hp, score, last_direction, bWIDTH):
        self.bWIDTH = bWIDTH
        self.width = width
        self.height = height
        self.VEL = vel
        self.image_uri = image_uri
        self.HP = hp
        self.score = score
        self.last_direction = last_direction
        self.controls = controls.Controls()
        PLAYER_CHARACTER_IMAGE = pygame.image.load(os.path.join(image_uri))
        self.PLAYER = pygame.transform.scale(PLAYER_CHARACTER_IMAGE, (self.width, self.height))
        self.x = self.bWIDTH/2 - self.width
        self.y = 450
        self.rect_player()

    
    def rect_player(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def __move(self):
        self.controls.key_listen()
        if self.controls.right and self.rect.x + self.VEL + self.width < self.bWIDTH + 80:
            self.rect.x += self.VEL
            self.last_direction = 'right'
        if self.controls.left and self.rect.x - self.VEL > -77:
            self.rect.x -= self.VEL
            self.last_direction = 'left'
        
        self.x = self.rect.x


    def __draw(self, WIN):
        if self.last_direction == 'left':
            flip = False
        elif self.last_direction == 'right':
            flip = True
        f_character = pygame.transform.flip(self.PLAYER, flip, False)
        WIN.blit(f_character, (self.x, self.y))

    
    def update(self, WIN):
        self.__move()
        self.__draw(WIN)
