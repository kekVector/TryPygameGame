import pygame
from settings import frame_size_x, frame_size_y, GREEN, WHITE, max_health_main_plain
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def sides_coord(list_coord):
    max_y = [list_coord[0][1], 0]
    max_x = [list_coord[0][0], 0]
    min_y = [list_coord[0][1], 0]
    min_x = [list_coord[0][0], 0]
    for count, elem in enumerate(list_coord):
        if elem[0] > max_x[0]:
            max_x[0] = elem[0]
            max_x[1] = count
        if elem[0] < min_x[0]:
            min_x[0] = elem[0]
            min_x[1] = count
        if elem[1] < max_y[0]:
            max_y[0] = elem[1]
            max_y[1] = count
        if elem[1] > min_y[0]:
            min_y[0] = elem[1]
            min_y[1] = count

    return max_x[1], min_x[1], max_y[1], min_y[1]


def is_shooted(plain_coord, bullets):
    index = []
    polygon = Polygon(plain_coord)
    if len(bullets) != 0:
        for count, elem in enumerate(bullets):
            if polygon.contains(Point(elem)) or polygon.contains(Point((elem[0], elem[1]-15))):
                index.append(count)

    return index


def show_score(score, choice, color, font, size, game_window):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)

    game_window.blit(score_surface, score_rect)


def draw_health(game_window, current_health):
    pygame.draw.rect(game_window, WHITE, (10, frame_size_y-37, 80, 20))
    pygame.draw.rect(game_window, GREEN, (12, frame_size_y-35, (current_health/max_health_main_plain)*76, 16))

# list_coord = [[160, 80], [148, 112], [132, 100], [128, 84],
#               [104, 116], [108, 132], [124, 148], [148, 148],
#               [160, 136], [172, 148], [196, 148], [212, 132],
#               [216, 116], [192, 84], [188, 100], [172, 112],
#               [160, 80]]
#
# max_x_index, min_x_index, max_y_index, min_y_index = sides_coord(list_coord)
# print(max_x_index, min_x_index, max_y_index, min_y_index)