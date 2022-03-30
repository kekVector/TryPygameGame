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
enemy_bullets = Bullets(game_window, direction='down')
plain_enemy = []
plain_enemy.append(Plain(plain_enemy_coord, game_window, plain_speed, random.choice(enemy_plains_color)))

score = 0
current_button = 't'
key_pressed = False
keyup = False
shoot_down = False
shoot_up = False
plain.resize(0.4)
plain_enemy[0].resize(0.2)
game_start = True

# game start
while game_start:
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
        if event.type == pygame.MOUSEBUTTONUP:
            shoot_down = False
            shoot_up = True
        if event.type == pygame.KEYUP:
            if event.key == ord(current_button):
                keyup = True
                key_pressed = False


# Fill area and start drawing from the beginning
    game_window.fill(BLACK)

    # Move main plain
    if key_pressed:
        plain.move(current_button)
    if keyup:
        plain.move(current_button)
        keyup = False

    # Shoot main plain
    if shoot_down:
        if plain.shoot_reload():
            plain_bullet.add_shoot(plain.get_start_coord(), (15,200, 200))
    if shoot_up:
        shoot_up = False


    # Shoot enemy plains
    for count, elem in enumerate(plain_enemy):
        if elem.shoot_reload():
            if random.random() <= 0.08:
                enemy_bullets.add_shoot(elem.get_start_coord(), 'random')

    # Destroy enemy plains
    for i in range(len(plain_enemy)-1, -1, -1):
        destroy_plain = is_shooted(plain_enemy[i].coord, plain_bullet.bullet_list)
        if len(destroy_plain) != 0:
            pygame.draw.polygon(game_window, BLACK, plain_enemy[i].coord)
            plain_enemy.pop(i)
            score += 1

    # Move enemy plains
    for plains in plain_enemy:
        if plains.right_side_coord() + speed >= frame_size_x:
            plains.re_swap(True)
        if plains.left_side_coord() - speed <= 0:
            plains.re_swap(False)
        if plains.swap:
            plains.move('a')
        else:
            plains.move('d')

    # Adding new enemy plain
    if pygame.time.get_ticks()%2000 <= clock.get_time() and pygame.time.get_ticks() > 2000:
        plain_enemy.append(Plain(plain_enemy_coord, game_window, speed=random.randint(4, 11),
                                 color=random.choice(enemy_plains_color),
                                 start_coord=(random.randint(200, 800), random.randint(50, 500))))
        plain_enemy[len(plain_enemy)-1].resize(random.uniform(0.2, 0.7))
    print(score)

    # Drawing
    for plains in plain_enemy:
        pygame.draw.polygon(game_window, plains.color, plains.coord)
    pygame.draw.polygon(game_window, WHITE, plain.coord)
    plain_bullet.draw()
    enemy_bullets.draw()
    show_score(score, 2, WHITE, 'consolas', 20, game_window)

    pygame.display.update()
    clock.tick(FPS)


