import pygame

class Text:
    def __init__(self, font, font_size, msg, color) -> None:
        self.text = msg
        self.color = color
        self.msg = msg
        self.SYSFONT = pygame.font.SysFont(font, font_size)
        self.text = self.get_text()


    def get_text(self):
        return self.SYSFONT.render(self.msg, True, self.color)


    def draw(self, WIN, x, y):
        WIN.blit(self.text, (x, y))