import random
import pygame
import time
import sys
from random import randint
from settings import *
from classes import *
from func import is_shooted, show_score

# start settings

pygame.init()
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
game_window.fill(BLACK)


plain = Plain(plain_coordinates, game_window, plain_speed)
plain_bullet = Bullets(game_window)
plain_enemy = []
plain_enemy.append(Plain(plain_enemy_coord, game_window, plain_speed, random.choice(enemy_plains_color)))
# game start

score = 0
current_button = 't'
key_pressed = False
keyup = False
shoot_down = False
shoot_up = False
plain.resize(0.4)
plain_enemy[0].resize(0.2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == ord('w'):
                current_button = 'w'
                key_pressed = True
            elif event.key == ord('a'):
                current_button = 'a'
                key_pressed = True
            elif event.key == ord('s'):
                current_button = 's'
                key_pressed = True
            elif event.key == ord('d'):
                current_button = 'd'
                key_pressed = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shoot_down = True
            shoot_reload = 5
        if event.type == pygame.MOUSEBUTTONUP:
            shoot_down = False
            shoot_up = True
        if event.type == pygame.KEYUP:
            if event.key == ord(current_button):
                keyup = True
                key_pressed = False


# Fill area and start drawing from the beginning
    # Moving objects

    game_window.fill(BLACK)
    if key_pressed:
        plain.move(current_button)
    if keyup:
        plain.move(current_button)
        keyup = False

    if shoot_down:
        if shoot_reload > 5:
            plain_bullet.add_shoot(plain.get_start_coord(), (15,200, 200))
            shoot_reload = 0
        else:
            shoot_reload += 1
    if shoot_up:
        shoot_up = False
    for i in range(len(plain_enemy)-1, -1, -1):
        destroy_plain = is_shooted(plain_enemy[i].left_side_coord(), plain_enemy[i].right_side_coord(),
                                   plain_enemy[i].up_side_coord(), plain_enemy[i].left_side_coord(),
                                   plain_bullet.bullet_list)
        if len(destroy_plain) != 0:
            pygame.draw.polygon(game_window, BLACK, plain_enemy[i].coord)
            plain_enemy.pop()
            score += 1

# Move enemy plain
    for plains in plain_enemy:
        if plains.right_side_coord() + speed >= frame_size_x:
            plains.re_swap(True)
        if plains.left_side_coord() - speed <= 0:
            plains.re_swap(False)

        if plains.swap:
            plains.move('a')
        else:
            plains.move('d')

    if pygame.time.get_ticks()%1000 <= clock.get_time() and pygame.time.get_ticks() > 2000:
        plain_enemy.append(Plain(plain_enemy_coord, game_window, plain_speed, random.choice(enemy_plains_color)))
        plain_enemy[len(plain_enemy)-1].resize(0.2)
    print(score)


    #drawing
    for plains in plain_enemy:
        pygame.draw.polygon(game_window, random.choice([RED, BLUE]), plains.coord)
    pygame.draw.polygon(game_window, WHITE, plain.coord)
    plain_bullet.draw()
    pygame.display.update()
    #show_score(score, 2, WHITE, 'consolas', 20, game_window)
    clock.tick(FPS)


