import random
import pygame
import time
import sys
from random import randint
from settings import *
from classes import *
from func import is_shooted, show_score, draw_health
import packets


def start_game():
    # start settings
    pygame.init()
    game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    game_window.fill(BLACK)

    plain = Plain(main_plain, game_window, plain_speed, start_coord=(frame_size_x / 2, frame_size_y - 100))
    plain_bullet = Bullets(game_window)
    enemy_bullets = Bullets(game_window, direction='down')
    plain_enemy = []
    health_spawn = []
    plain_enemy.append(Plain(plain_enemy_2, game_window, plain_speed, random.choice(enemy_plains_color)))

    score = 0
    current_button = 't'
    key_pressed = False
    keyup = False
    shoot_down = False
    shoot_up = False
    game_start = True
    font_stars = FontSpace(1.7, 10)
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
                elif event.key == pygame.K_ESCAPE:
                    packets.pause()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                shoot_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                shoot_down = False
                shoot_up = True
            if event.type == pygame.KEYUP:
                if event.key == ord(current_button):
                    keyup = True
                    key_pressed = False
        print(plain_enemy[0].current_move_dir)
        # Fill area and start drawing from the beginning
        game_window.fill(BLACK)
        font_stars.font_move(game_window)
        # Move main plain
        if key_pressed:
            plain.move(current_button)
        if keyup:
            plain.move(current_button)
            keyup = False

        # Shoot main plain
        if shoot_down:
            if plain.shoot_reload():
                plain_bullet.add_shoot(plain.get_shoot_coord(), (15, 200, 200), 'line', speed=15)
        if shoot_up:
            shoot_up = False

        # Shoot enemy plains
        for count, elem in enumerate(plain_enemy):
            if elem.shoot_reload():
                if random.random() <= 0.08:
                    enemy_bullets.add_shoot(elem.get_shoot_coord(), 'random', random.choice(['line', 'circle']))

        # Destroy enemy plains
        for i in range(len(plain_enemy) - 1, -1, -1):
            destroy_plain = is_shooted(plain_enemy[i].coord, plain_bullet.bullet_coords)
            if len(destroy_plain) != 0:
                pygame.draw.polygon(game_window, BLACK, plain_enemy[i].coord)
                plain_enemy[i].current_hp -= 1
                if plain_enemy[i].current_hp <= 0:
                    score += 1
                    plain_enemy.pop(i)
                else:
                    plain_enemy[i].hit(1)
                for i in destroy_plain:
                    plain_bullet.del_bullet(i)

        # Lose health on hit
        destroy_plain = is_shooted(plain.coord, enemy_bullets.bullet_coords)
        if len(destroy_plain) != 0:
            # plain.current_hp -= 1
            for i in destroy_plain:
                enemy_bullets.del_bullet(i)
        if plain.current_hp <= 0:
            game_start = False

        # Get healths
        for i in range(len(health_spawn) - 1, -1, -1):
            get_health = is_shooted(plain.coord, [health_spawn[i].coord_circle])
            if len(get_health) != 0:
                plain.get_hp(health_spawn[i].value_health)
                health_spawn.pop(i)

        # Move enemy plains
        for plains in plain_enemy:
            plains.random_move()
            plains.draw(game_window)
            # if plains.right_side_coord() + speed >= frame_size_x:
            #     plains.re_swap(True)
            # if plains.left_side_coord() - speed <= 0:
            #     plains.re_swap(False)
            # if plains.swap:
            #     plains.move('a')
            # else:
            #     plains.move('d')
        ######
        # Adding new enemy plain
        if pygame.time.get_ticks() % 1500 <= clock.get_time() and pygame.time.get_ticks() > 2000:
            plain_enemy.append(
                Plain(random.choice((plain_enemy_1, plain_enemy_2, plain_enemy_3, plain_enemy_4)), game_window,
                      speed=random.randint(4, 8),
                      color=random.choice(enemy_plains_color),
                      start_coord=(random.randint(200, 800), random.randint(50, 500)),
                      hp=random.randint(3, 4)))
            plain_enemy[len(plain_enemy) - 1].resize(random.uniform(1, 2.5))

        # Adding health
        if random.random() <= 0.003:
            health_spawn.append(HealthSphere(game_window))

        # Drawing
        for plains in plain_enemy:
            plains.draw(game_window)
        for health in health_spawn:
            health.draw()
        plain.draw(game_window)
        plain_bullet.draw()
        enemy_bullets.draw()
        show_score(score, 2, WHITE, 'consolas', 20, game_window)
        draw_health(game_window, plain.current_hp)
        pygame.display.update()
        clock.tick(FPS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        game_window.fill(BLACK)
        show_score(score, 2, WHITE, 'consolas', 20, game_window)
        pygame.display.update()


if __name__ == '__main__':
    start_game()
