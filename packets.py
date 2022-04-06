from classes import ButtonMenu
from settings import *
import pygame
import main
import menu

pause_size_x = frame_size_x
pause_size_y = frame_size_y
pygame.init()
button_pause_resum = ButtonMenu(button_pause_resum_color, button_pause_resum_color_text,
                                btn_coord=[pause_size_x / 6, (pause_size_y / 20)],
                                btn_text="RESUM", btn_height=(pause_size_y / 9),
                                btn_width=(frame_size_x / 6) * 4, txt_size=100
                                )

button_pause_restart = ButtonMenu(button_pause_restart_color, button_pause_restart_color_text,
                                  btn_coord=[button_pause_resum.x_start_coord, button_pause_resum.y_start_coord + 1.2*(button_pause_resum.height)],
                                  btn_text="RESTART", btn_height=button_pause_resum.height,
                                  btn_width=button_pause_resum.width, txt_size=100
                                  )

button_pause_main_menu = ButtonMenu(button_pause_main_menu_color, button_pause_main_menu_color_text,
                                    btn_coord=[button_pause_resum.x_start_coord, button_pause_resum.y_start_coord + 2.4*(button_pause_resum.height)],
                                    btn_text="MAIN MENU", btn_height=button_pause_resum.height,
                                    btn_width=button_pause_resum.width, txt_size=100
                                    )

button_pause_exit = ButtonMenu(button_pause_exit_color, button_pause_exit_color_text,
                               btn_coord=[button_pause_resum.x_start_coord, button_pause_resum.y_start_coord + 3.6*(button_pause_resum.height)],
                               btn_text="EXIT", btn_height=button_pause_resum.height,
                               btn_width=button_pause_resum.width, txt_size=100
                               )


def pause():

    game_window = pygame.display.set_mode((pause_size_x, pause_size_y - 300))
    pygame.display.set_caption("Pause")
    clock = pygame.time.Clock()
    game_window.fill(BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                button_pause_resum.tapped = button_pause_resum.is_point_on_button(event.pos)
                button_pause_restart.tapped = button_pause_restart.is_point_on_button(event.pos)
                button_pause_main_menu.tapped = button_pause_main_menu.is_point_on_button(event.pos)
                button_pause_exit.tapped = button_pause_exit.is_point_on_button(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if button_pause_resum.is_point_on_button(event.pos):
                        return
                    elif button_pause_restart.is_point_on_button(event.pos):
                        main.start_game()
                    elif button_pause_main_menu.is_point_on_button(event.pos):
                        menu.menu()
                    elif button_pause_exit.is_point_on_button(event.pos):
                        pygame.quit()

        game_window.fill(BLACK)
        button_pause_resum.draw(game_window)
        button_pause_restart.draw(game_window)
        button_pause_main_menu.draw(game_window)
        button_pause_exit.draw(game_window)

        pygame.display.update()
        clock.tick(10)
