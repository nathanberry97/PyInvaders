import pygame
from enemy import enemy


class enemy_manager:
    def __init__(self, display: pygame.Surface):
        self.display = display
        self.enemy_dict = {}

    def create_enemies(self):
        """Method to create enemies"""

        x_axis = 100
        y_axis = 75

        for count in range(11):
            self.enemy_dict[count] = enemy(self.display, x_axis, y_axis)
            x_axis += 175

            if count == 3:
                y_axis = 175
                x_axis = 175

            elif count == 6:
                y_axis = 275
                x_axis = 100

    def draw_enemies(self):
        """Method to draw enemies in dict to the display"""

        for enemy_object in self.enemy_dict:
            self.enemy_dict[enemy_object].draw_enemy()

    def get_enemies_objects(self) -> dict:
        """Method to return enemy dict"""

        return self.enemy_dict
