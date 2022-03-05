import pygame
import settings
import random
from func import sides_coord
frame_size_x = settings.frame_size_x
frame_size_y = settings.frame_size_y


class Plain:
    def __init__(self, list_coord, game_window, speed=7, swap = False):
        self.game_window = game_window
        self.speed = speed
        self.coord_start = [list_coord[0][0], list_coord[0][1]]
        self.coord = list_coord
        self.max_x_index, self.min_x_index, self.max_y_index, self.min_y_index = sides_coord(self.coord)
        self.swap = swap
        self.alive = True

    def resize(self, k):
        for count, i in enumerate(self.coord):
            for count2, j in enumerate(i):
                self.coord[count][count2] = int(float(j) * k)

    def get_start_coord(self):
        return [self.coord[0][0], self.coord[0][1]]

    def get_coord(self):
        return self.coord

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
            if self.coord[self.min_y_index][1] + self.speed < settings.frame_size_y:
                for coord in self.coord:
                    coord[1] += self.speed
        elif button == 'd':
            if self.coord[self.max_x_index][0] + self.speed < settings.frame_size_x:
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

    def Swap(self, *arg):
        if len(arg) == 0:
            self.swap = not (self.swap)
        else:
            self.swap = arg[0]

    def is_swap(self):
        return self.swap

    def die(self):
        self.alive = False

    def is_alive(self):
        return self.alive


class Bullets:
    def __init__(self, game_window):
        self.bullet_list = []
        self.color_list = []
        self.game_window = game_window

    def add_shoot(self, coord_start, color):
        self.bullet_list.insert(0, coord_start)
        self.color_list.insert(0, color)

    def draw(self):
        for count, elem in enumerate(self.bullet_list):
            pygame.draw.line(self.game_window, self.color_list[count] if self.color_list[count] != 'random' else
                             random.choice([settings.RED, settings.GREEN, settings.BLUE]), elem,
                             [elem[0], elem[1] - 15], 3)
            elem[1] -= 15
            if elem[1] <= 0:
                self.bullet_list.pop()
                self.color_list.pop()

    def del_bullet(self, index):
        del self.bullet_list[index]

    def bullets(self):
        return self.bullet_list