import pygame

class Controls:
    def __init__(self) -> None:
        self.left = False
        self.right = False
        self.key_listen()

    def key_listen(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.right = True
        else:
            self.right = False
        if keys_pressed[pygame.K_LEFT]:
            self.left = True
        else:
            self.left = False