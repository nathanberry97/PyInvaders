import pygame
from base_config import base_config
from player import player


class game_logic:
    def __init__(self):
        self.base = base_config(800, 720)
        self.screen = self.base.configure_screen()
        self.player = player(self.screen)

        self.background = self.base.import_background("background_score.png")
        self.space = self.base.import_background("background_space.png")
        self.fps = 60

        self.x_axis = 50
        self.y_axis = [50, -500, -1000]

    def main_loop(self) -> None:
        """The main loop of the game"""

        game_loop = True

        while game_loop:
            self.base.set_frame_rate(self.fps)

            for space in self.y_axis:
                self.screen.blit(self.space, (self.x_axis, space))

            self.y_axis = self.base.update_screen(self.y_axis)

            self.player.draw_player()

            self.player.move_player()

            self.player.laser_dict(self.player.get_coordinates())

            self.player.draw_laser()

            self.player.move_laser()

            self.screen.blit(self.background, (0, 0))

            self.player.draw_laser_charge()

            self.player.draw_life_icon()

            game_loop = self.base.quit_game()

            pygame.display.update()
