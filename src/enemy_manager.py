import pygame
from enemy import enemy


class enemy_manager:
    def __init__(self, display: pygame.Surface):
        self.display = display
        self.enemy_dict = {}
        self.game_level = 0
        self.score = 0
        self.privous_enemy_count = 0

    def create_enemies(self):
        """Method to create enemies"""

        self.game_level += 1
        self.privous_enemy_count = 11

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

    def draw_enemies(self, player, object_player):
        """Method to draw enemies in dict to the display"""

        for enemy_object in self.enemy_dict:
            self.enemy_dict[enemy_object].draw_enemy()
            self.enemy_dict[enemy_object].shoot_laser(player, object_player)

    def update_score(self):
        """Method to update the current score"""

        current_enemy_count = len(self.enemy_dict)

        if current_enemy_count != self.privous_enemy_count:
            self.score += 5
            self.privous_enemy_count = current_enemy_count

    def get_enemies_objects(self) -> dict:
        """Method to return enemy dict"""

        return self.enemy_dict

    def get_level(self) -> int:
        """Method to return current level"""

        return self.game_level

    def get_score(self) -> int:
        """Method to return current level"""

        return self.score

    def reset_variables(self) -> None:
        """Method to return current level"""

        self.score = 0
        self.game_level = 0
