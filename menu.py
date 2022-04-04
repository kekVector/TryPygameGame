import pygame
from settings import *
import main


pygame.init()
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption("Airplane")
clock = pygame.time.Clock()
game_window.fill(BLACK)
button_click = False
start_menu_change = False
start_exit_change = False
# Text settings
start_button_color = (50, 205, 50)
font_start_button = pygame.font.Font(None, 128)
text_start_button = font_start_button.render("START GAME", True, start_button_color)
place_start_button = text_start_button.get_rect(center=(frame_size_x/2, frame_size_y/4.5))

exit_button_color = (178, 34, 34)
font_exit_button = pygame.font.Font(None, 128)
text_exit_button = font_exit_button.render("EXIT", True, exit_button_color)
place_exit_button = text_exit_button.get_rect(center=(frame_size_x/2, (frame_size_y/9)*5))


while not button_click:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            if ((button_menu_start_coord[0] + button_menu_width) >= event.pos[0] >= button_menu_start_coord[0]) and\
                    ((button_menu_start_coord[1] + button_menu_height) >= event.pos[1] >= button_menu_start_coord[1]):
                start_menu_change = True
            else:
                start_menu_change = False
            if (button_exit_start_coord[0] + button_exit_width >= event.pos[0] >= button_exit_start_coord[0]) and\
                    (button_exit_start_coord[1] + button_exit_height >= event.pos[1] >= button_exit_start_coord[1]):
                start_exit_change = True
            else:
                start_exit_change = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ((button_menu_start_coord[0] + button_menu_width) >= event.pos[0] >= button_menu_start_coord[0]) and \
                    ((button_menu_start_coord[1] + button_menu_height) >= event.pos[1] >= button_menu_start_coord[1]):
                main.start_game()
            elif (button_exit_start_coord[0] + button_exit_width >= event.pos[0] >= button_exit_start_coord[0]) and \
                    (button_exit_start_coord[1] + button_exit_height >= event.pos[1] >= button_exit_start_coord[1]):
                pygame.quit()

    game_window.fill(BLACK)

    # Draw start_button
    pygame.draw.rect(game_window, start_button_color, (button_menu_start_coord[0], button_menu_start_coord[1],
                     button_menu_width, button_menu_height), 10)

    if start_menu_change:
        pygame.draw.rect(game_window, WHITE, (button_menu_start_coord[0], button_menu_start_coord[1],
                                              button_menu_width, button_menu_height), 3)
        font_start_button = pygame.font.Font(None, 118)
        text_start_button = font_start_button.render("START GAME", True, start_button_color)
        place_start_button = text_start_button.get_rect(center=(frame_size_x / 2, frame_size_y / 4.5))
    else:
        font_start_button = pygame.font.Font(None, 128)
        text_start_button = font_start_button.render("START GAME", True, start_button_color)
        place_start_button = text_start_button.get_rect(center=(frame_size_x / 2, frame_size_y / 4.5))
    game_window.blit(text_start_button, place_start_button)

    # Draw exit Button
    pygame.draw.rect(game_window, exit_button_color, (button_exit_start_coord[0], button_exit_start_coord[1],
                     button_exit_width, button_exit_height), 10)
    if start_exit_change:
        pygame.draw.rect(game_window, WHITE, (button_exit_start_coord[0], button_exit_start_coord[1],
                                              button_exit_width, button_exit_height), 2)
        font_exit_button = pygame.font.Font(None, 118)
        text_exit_button = font_exit_button.render("EXIT", True, exit_button_color)
        place_exit_button = text_exit_button.get_rect(center=(frame_size_x / 2, (frame_size_y / 9) * 5))
    else:
        font_exit_button = pygame.font.Font(None, 128)
        text_exit_button = font_exit_button.render("EXIT", True, exit_button_color)
        place_exit_button = text_exit_button.get_rect(center=(frame_size_x / 2, (frame_size_y / 9) * 5))
    game_window.blit(text_exit_button, place_exit_button)

    pygame.display.update()
    clock.tick(10)
