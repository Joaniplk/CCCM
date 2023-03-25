import os
import pygame
import time
import classes.drop as drop
import classes.player as player
import classes.text as txt

pygame.font.init()
WIDTH, HEIGHT = 1300, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Christmas Candy Collection Simulator 1.0")
D_YELLOW = (50, 50, 22)
red = (255, 50, 50)
FPS = 60
VEL, CO_VEL, CA_VEL = 6.5, 5, 3
PLAYERWIDTH, PLAYERHEIGHT, DROPWIDTH, DROPHEIGHT = 156, 256, 64, 64
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Xmas_background.png')), (WIDTH, HEIGHT))

COAL = drop.Drop(DROPWIDTH, DROPHEIGHT, 0, 0, CO_VEL, 'coaldrop.png', WIDTH)
CANDY = drop.Drop(DROPWIDTH, DROPHEIGHT, 0, 0, CA_VEL, 'candycanedrop.png', WIDTH)
PLAYER = player.Player(PLAYERWIDTH, PLAYERHEIGHT, VEL, 'present character1.png', 5, 0, 'left', WIDTH)


def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        # Closing the game with the 'X'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        GAME_OVER_TXT = txt.Text('sans', 80, "You lost!", red)
        SCORE_TXT = txt.Text('Verdana', 40, "Your Score: " + str(PLAYER.score), D_YELLOW)
        HP_TXT = txt.Text('Verdana', 40, "HitPoints: " + str(PLAYER.HP), D_YELLOW)
        if PLAYER.HP <= 0:
            GAME_OVER_TXT.draw(WIN, WIDTH / 2 - GAME_OVER_TXT.text.get_width() / 2, HEIGHT / 2 - GAME_OVER_TXT.text.get_height())
            pygame.display.update()
            time.sleep(1.75)
            running = False
        PLAYER.move()
        if  COAL.rect.colliderect(PLAYER.rect):
            PLAYER.HP -= 1
            COAL.reset_rect()
        if CANDY.rect.colliderect(PLAYER.rect):
            PLAYER.score += 1
            CANDY.reset_rect()
        if CANDY.rect.y > HEIGHT:
            PLAYER.HP -= 1
            CANDY.reset_rect()
        if COAL.rect.y > HEIGHT:
            COAL.reset_rect()
        WIN.blit(BACKGROUND, (0, 0))
        CANDY.update_drop(WIN)
        COAL.update_drop(WIN)
        PLAYER.draw(WIN)
        HP_TXT.draw(WIN, WIDTH - HP_TXT.text.get_width() - 10, 10)
        SCORE_TXT.draw(WIN, 0, 0)
        pygame.display.update()


if __name__ == "__main__":
    main()
