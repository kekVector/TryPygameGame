import pygame
from settings import *
import main
from classes import ButtonMenu


def menu():
    pygame.init()
    game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
    pygame.display.set_caption("Airplane")
    clock = pygame.time.Clock()
    game_window.fill(BLACK)

    # Buttons settings

    button_start_game = ButtonMenu(start_button_color, start_button_color,
                                   btn_coord=[frame_size_x / 6, frame_size_y / 18],
                                   btn_text="START GAME", btn_height=(frame_size_y / 9) * 2,
                                   btn_width=(frame_size_x / 6) * 4
                                   )

    button_exit = ButtonMenu(exit_button_color, exit_button_text_color,
                             btn_coord=[button_start_game.x_start_coord, (frame_size_y / 9) * 5],
                             btn_text="EXIT", btn_height=button_start_game.height,
                             btn_width=button_start_game.width
                             )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                button_start_game.tapped = button_start_game.is_point_on_button(event.pos)
                button_exit.tapped = button_exit.is_point_on_button(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_start_game.is_point_on_button(event.pos):
                    main.start_game()
                elif button_exit.is_point_on_button(event.pos):
                    pygame.quit()

        game_window.fill(BLACK)
        button_start_game.draw(game_window)
        button_exit.draw(game_window)

        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    menu()
