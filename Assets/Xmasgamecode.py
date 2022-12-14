import random
import os
import pygame
import time
pygame.font.init()
WIDTH, HEIGHT = 1300, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Christmas Candy Collection Simulator 1.0")
white = (255, 255, 255)
D_YELLOW = (50, 50, 22)
red = (255, 50, 50)
green = (40, 255, 50)
HITPOINTS_FONT = pygame.font.SysFont('Verdana', 40)  # NOQA
SCORE_FONT = pygame.font.SysFont('Verdana', 40)
END_FONT = pygame.font.SysFont('sans', 80)
FPS = 60
VEL, Co_VEL, Ca_VEL = 6.5, 5, 3
PLAYERWIDTH, PLAYERHEIGHT, DROPWIDTH, DROPHEIGHT = 156, 256, 64, 64  # NOQA
CANDY_IMAGE = pygame.image.load(os.path.join('candycanedrop.png'))  # NOQA
CANDY = pygame.transform.scale(CANDY_IMAGE, (DROPWIDTH, DROPHEIGHT))
PLAYER_CHARACTER_IMAGE = pygame.image.load(os.path.join('present character1.png'))
PLAYER_CHARACTER = pygame.transform.scale(PLAYER_CHARACTER_IMAGE, (PLAYERWIDTH, PLAYERHEIGHT))
COAL_IMAGE = pygame.image.load(os.path.join('coaldrop.png'))  # NOQA
COAL = pygame.transform.scale(COAL_IMAGE, (DROPWIDTH, DROPHEIGHT))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Xmas_background.png')), (WIDTH, HEIGHT))


def main():
    dropy = 0
    candyx = round(random.randrange(300, WIDTH - 100))  # NOQA
    coalx = round(random.randrange(300, WIDTH - 100))  # NOQA
    last_direction = 'left'
    game_over_text = END_FONT.render('You lost! ', True, red)
    score = 0
    hp = 100
    character = pygame.Rect(WIDTH/2 - PLAYERWIDTH, 400, PLAYERWIDTH, PLAYERHEIGHT)
    candy = pygame.Rect(candyx, dropy, DROPWIDTH, DROPHEIGHT)
    coal = pygame.Rect(coalx, dropy, DROPWIDTH, DROPHEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Closing the game with the 'X'
                run = False
        if hp < 0:
            end_text = 'You lost!'
            WIN.blit(game_over_text, (WIDTH / 2 - game_over_text.get_width(), HEIGHT / 2 - game_over_text.get_height()))
            pygame.display.update()
            time.sleep(1.75)
            print(end_text)
            run = False
        keys_pressed = pygame.key.get_pressed()    # Player movement
        if keys_pressed[pygame.K_RIGHT] and character.x + VEL + PLAYERWIDTH < WIDTH + 80:
            character.x += VEL
            last_direction = 'right'
        if keys_pressed[pygame.K_LEFT] and character.x - VEL > -77:
            character.x -= VEL
            last_direction = 'left'
        if coal.colliderect(character):
            hp -= 1
        elif candy.colliderect(character):
            score += 1
            candy.y = 0
            candy.x = round(random.randrange(300, WIDTH - 100))
            coal.y = 0
            coal.x = round(random.randrange(300, WIDTH - 100))
        elif candy.y > HEIGHT:
            hp -= 10
        if last_direction == 'left':
            hitpoints_text = HITPOINTS_FONT.render('HitPoints: ' + str(hp), True, D_YELLOW)  # NOQA
            score_text = SCORE_FONT.render('Your Score: ' + str(score), True, D_YELLOW)
            coal.y += Co_VEL
            candy.y += Ca_VEL
            f_character = pygame.transform.flip(PLAYER_CHARACTER, False, False)  # character rotation to match movement
            WIN.blit(BACKGROUND, (0, 0))
            WIN.blit(f_character, (character.x, character.y))
            WIN.blit(CANDY, (candy.x, candy.y))
            WIN.blit(COAL, (coal.x, coal.y))
            WIN.blit(hitpoints_text, (WIDTH - hitpoints_text.get_width() - 10, 10))
            WIN.blit(score_text, (0, 0))
        pygame.display.update()
        if coal.colliderect(character):
            hp -= 1
        if candy.colliderect(character):
            score += 1
            candy.y = 0
            candy.x = round(random.randrange(300, WIDTH - 100))
            coal.y = 0
            coal.x = round(random.randrange(300, WIDTH - 100))
        elif candy.y > HEIGHT:
            hp -= 10
        if last_direction == 'right':
            hitpoints_text = HITPOINTS_FONT.render('HitPoints: ' + str(hp), True, D_YELLOW)  # NOQA
            score_text = SCORE_FONT.render('Your Score: ' + str(score), True, D_YELLOW)
            coal.y += Co_VEL
            candy.y += Ca_VEL
            f_character = pygame.transform.flip(PLAYER_CHARACTER, True, False)
            WIN.blit(BACKGROUND, (0, 0))
            WIN.blit(f_character, (character.x, character.y))
            WIN.blit(CANDY, (candy.x, candy.y))
            WIN.blit(COAL, (coal.x, coal.y))
            WIN.blit(hitpoints_text, (WIDTH - hitpoints_text.get_width() - 10, 10))
            WIN.blit(score_text, (0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()
