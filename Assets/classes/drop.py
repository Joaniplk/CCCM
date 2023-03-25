import pygame
import os
import random

class Drop:
    def __init__(self, width, height, x, y, vel, imageUri, boardWidth):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vel = vel
        self.imageUri = imageUri
        self.boardWidth = boardWidth
        DROP_IMAGE = pygame.image.load(os.path.join(imageUri))
        self.image = pygame.transform.scale(DROP_IMAGE, (self.width, self.height))
        self.x = self.get_drop_x(300, 100)
        self.rect_drop()


    def rect_drop(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    
    def get_drop_x(self, start, end):
        return round(random.randrange(start, self.boardWidth - end))


    def reset_rect(self):
        self.rect.y = 0
        self.rect.x = self.get_drop_x(300, 100)
        self.x = self.rect.x
        self.y = 0
    
    def draw(self, WIN):
        WIN.blit(self.image, (self.x, self.y))


    def update_drop(self, WIN):
        self.rect.y += self.vel
        self.y += self.vel
        self.draw(WIN)
