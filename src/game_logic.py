import pygame
from base_config import base_config


class game_logic:
    def __init__(self):
        self.base = base_config(800, 720)
        self.screen = self.base.configure_screen()

        self.background = self.base.import_background("background_score.png")
        self.space = self.base.import_background("background_space.png")
        self.fps = 60

        self.y_axis = [50, -575, -1150]

    def main_loop(self) -> None:
        """The main loop of the game"""

        game_loop = True

        while game_loop:
            pygame.display.update()

            self.base.set_frame_rate(self.fps)

            for space in self.y_axis:
                self.screen.blit(self.space, (50, space))

            self.screen.blit(self.background, (0, 0))

            self.update_screen()

            game_loop = self.base.quit_game()

    def update_screen(self):
        """Ensure that space background moves"""

        for i, axis in enumerate(self.y_axis):
            self.y_axis[i] += 1

            if axis >= 700:
                self.y_axis[i] = -1150
