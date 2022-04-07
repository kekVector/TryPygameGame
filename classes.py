import pygame
from settings import *
import random
from func import sides_coord


class Plain:
    def __init__(self, list_coord, game_window, speed=7, swap=False, color=RED, start_coord=False, cooldown=5, hp=10):
        self.coord = []
        self.game_window = game_window
        self.speed = speed
        self.max_health = hp
        self.current_hp = hp
        if start_coord:
            x_diff = start_coord[0] - list_coord[0][0]
            y_diff = start_coord[1] - list_coord[0][0]
        else:
            x_diff = 0
            y_diff = 0
        for i in list_coord:
            self.coord.append([i[0] + x_diff, i[1] + y_diff])
        self.max_x_index, self.min_x_index, self.max_y_index, self.min_y_index = sides_coord(self.coord)
        self.swap = swap
        self.alive = True
        self.color = color
        self.cooldown = cooldown
        self.current_cooldown = cooldown

    def shoot_reload(self):
        if self.current_cooldown >= self.cooldown:
            self.current_cooldown = 0
            return True
        else:
            self.current_cooldown += 1
            return False

    def replace(self, start_coord):
        x_diff = start_coord[0] - self.coord[0][0]
        y_diff = start_coord[1] - self.coord[0][1]
        for i in range(len(self.coord)):
            self.coord[i][0] += x_diff
            self.coord[i][1] += y_diff

    def resize(self, k):
        for count, i in enumerate(self.coord):
            for count2, j in enumerate(i):
                self.coord[count][count2] = int(float(j) * k)

    def get_start_coord(self):
        return [self.coord[0][0], self.coord[0][1]]

    def move(self, button):
        if button == 'w':
            if self.coord[self.max_y_index][1] - self.speed > 0:
                for coord in self.coord:
                    coord[1] -= self.speed
        elif button == 'a':
            if self.coord[self.min_x_index][0] - self.speed > 0:
                for coord in self.coord:
                    coord[0] -= self.speed
        elif button == 's':
            if self.coord[self.min_y_index][1] + self.speed < frame_size_y:
                for coord in self.coord:
                    coord[1] += self.speed
        elif button == 'd':
            if self.coord[self.max_x_index][0] + self.speed < frame_size_x:
                for coord in self.coord:
                    coord[0] += self.speed

    def up_side_coord(self):
        return self.coord[self.max_y_index][1]

    def down_side_coord(self):
        return self.coord[self.min_y_index][1]

    def right_side_coord(self):
        return self.coord[self.max_x_index][0]

    def left_side_coord(self):
        return self.coord[self.min_x_index][0]

    def re_swap(self, *arg):
        if len(arg) == 0:
            self.swap = not self.swap
        else:
            self.swap = arg[0]

    def die(self):
        self.alive = False

    def get_hp(self, hp):
        if self.current_hp + hp >= self.max_health:
            self.current_hp = self.max_health
        else:
            self.current_hp += hp


class Bullets:
    def __init__(self, game_window, direction='up'):
        self.bullet_list = []
        self.color_list = []
        self.game_window = game_window
        if direction == 'up':
            self.direction = 1
        else:
            self.direction = -1

    def add_shoot(self, coord_start, color):
        self.bullet_list.insert(0, coord_start)
        self.color_list.insert(0, color)

    def draw(self):
        for count, elem in enumerate(self.bullet_list):
            pygame.draw.line(self.game_window, self.color_list[count] if self.color_list[count] != 'random' else
            random.choice([RED, GREEN, BLUE]), elem, [elem[0], (elem[1] + self.direction * (-15))], 3)
            elem[1] -= 15 * self.direction
            if elem[1] <= 0 or elem[1] >= frame_size_y:
                self.bullet_list.pop(count)
                self.color_list.pop(count)

    def del_bullet(self, index):
        del self.bullet_list[index]


class HealthSphere:
    def __init__(self, game_window, speed=2, value=3, start_coord='random', color=[WHITE, GREEN]):
        self.coord_plus = [[10, 0], [20, 0], [20, 10], [30, 10], [30, 20], [20, 20], [20, 30],
                           [10, 30], [10, 20], [0, 20], [0, 10], [10, 10], [10, 0]]
        self.color_plus = color[0]
        self.color_circle = color[1]
        self.coord_circle = [15, 15]
        self.radius = 17
        self.replace([random.randint(30, frame_size_x - 30), 20] if start_coord == 'random' else start_coord)
        self.speed = speed
        self.value_health = value
        self.game_window = game_window

    def replace(self, start_coord):
        x_diff = start_coord[0] - self.coord_plus[0][0]
        y_diff = start_coord[1] - self.coord_plus[0][1]
        for i in range(len(self.coord_plus)):
            self.coord_plus[i][0] += x_diff
            self.coord_plus[i][1] += y_diff
        self.coord_circle[0] = self.coord_plus[0][0] + 5
        self.coord_circle[1] = self.coord_plus[0][1] + 15

    def draw(self):
        self.coord_circle[1] += self.speed
        for count, elem in enumerate(self.coord_plus):
            self.coord_plus[count][1] += self.speed
        pygame.draw.circle(self.game_window, self.color_circle, self.coord_circle, self.radius)
        pygame.draw.polygon(self.game_window, self.color_plus, self.coord_plus)


class ButtonMenu:

    def __init__(self, color_btn, color_txt, btn_coord, btn_text: str, btn_height, btn_width, txt_size=128,
                 txt_font=None, rect_fat=10):
        self.tapped = False
        self.x_start_coord = btn_coord[0]
        self.y_start_coord = btn_coord[1]
        self.height = int(btn_height)
        self.width = int(btn_width)
        self.color_btn = color_btn
        self.color_txt = color_txt
        self.txt_size = txt_size
        self.text_resize = 10
        self.rect_fat = rect_fat

        # Make text settings when button down
        self.text_button_down = pygame.font.Font(txt_font, self.txt_size - 10).render(btn_text, True, self.color_txt)
        self.place_button_down = self.text_button_down.get_rect(
            center=((btn_width / 2) + btn_coord[0], (btn_height / 2) + btn_coord[1]))

        # Make text settings when button up
        self.text_button_up = pygame.font.Font(txt_font, self.txt_size).render(btn_text, True, self.color_txt)
        self.place_button_up = self.text_button_up.get_rect(
            center=(btn_width / 2 + btn_coord[0], btn_height / 2 + btn_coord[1]))

        self.button_rect = pygame.Rect((btn_coord[0], btn_coord[1], btn_width, btn_height))

    def draw_up_button(self, game_window):
        pygame.draw.rect(game_window, self.color_btn, self.button_rect, self.rect_fat)
        game_window.blit(self.text_button_up, self.place_button_up)

    def draw_down_button(self, game_window):
        pygame.draw.rect(game_window, self.color_btn, self.button_rect, self.rect_fat)
        pygame.draw.rect(game_window, WHITE, self.button_rect, self.rect_fat // 3)
        game_window.blit(self.text_button_down, self.place_button_down)

    def is_point_on_button(self, point):
        return ((self.x_start_coord + self.width) >= point[0] >= self.x_start_coord) and \
               ((self.y_start_coord + self.height) >= point[1] >= self.y_start_coord)

    def draw(self, game_window):
        if self.tapped:
            self.draw_down_button(game_window)
        else:
            self.draw_up_button(game_window)


class FontSpace:
    def __init__(self, move_speed, frequency, r=2):
        self.move_speed = move_speed
        self.frequency = frequency
        self.radius = r
        self.stars = []
        for y in range(0, frame_size_y, frequency):
            self.stars.append([random.randint(3, frame_size_x - 1), y])

    def font_move(self, game_window):
        if self.stars[0][1] >= self.frequency:
            self.stars.insert(0, [random.randint(3, frame_size_x - 1), 0])
            if random.random() <= 0.001:
                self.stars.insert(0, [random.randint(3, frame_size_x - 1), 0])
        for i in range(len(self.stars) - 1, -1, -1):
            self.stars[i][1] += self.move_speed
            if self.stars[i][1] >= frame_size_y:
                self.stars.pop(i)
            else:
                pygame.draw.circle(game_window, WHITE, self.stars[i], self.radius)
