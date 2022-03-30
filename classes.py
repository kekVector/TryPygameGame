import pygame
from settings import *
import random
from func import sides_coord


class Plain:
    def __init__(self, list_coord, game_window, speed=7, swap=False, color=RED, start_coord=False, cooldown=5):
        self.coord = []
        self.game_window = game_window
        self.speed = speed
        #self.coord_start = [list_coord[0][0], list_coord[0][1]]
        if start_coord:
            x_diff = start_coord[0] - list_coord[0][0]
            y_diff = start_coord[1] - list_coord[0][0]
        else:
            x_diff = 0
            y_diff = 0
        for i in list_coord:
            self.coord.append([i[0]+x_diff, i[1]+y_diff])
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
            if self.coord[self.max_y_index][1]-self.speed > 0:
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


class Bullets:
    def __init__(self, game_window,  direction = 'up'):
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
                             random.choice([RED, GREEN, BLUE]), elem,
                             [elem[0], (elem[1] + self.direction*(-15))], 3)
            elem[1] -= 15*self.direction
            if elem[1] <= 0 or elem[1] >= frame_size_y:
                self.bullet_list.pop(count)
                self.color_list.pop(count)

    def del_bullet(self, index):
        del self.bullet_list[index]
