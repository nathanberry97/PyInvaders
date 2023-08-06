import pygame
import random


class enemy:
    def __init__(self, display: pygame.Surface, x_axis: int, y_axis: int):
        self.display = display

        self.count = 0
        self.count_check = False

        self.y_axis_counter = 450
        self.y_axis = y_axis - self.y_axis_counter
        self.x_axis = x_axis
        self.scale = 5

        self.frame_one = "../assets/alien_one.png"
        self.frame_two = "../assets/alien_two.png"
        self.frame_three = "../assets/alien_three.png"
        self.frame_four = "../assets/alien_four.png"

        self.rect = pygame.Rect

        self.state = 1
        self.update_interval = 100
        self.frame_interval = 0

        self.laser = "../assets/enemy_laser.png"
        self.laser_coordinates = []

    def draw_enemy(self):
        """Method to draw the player on the screen"""

        frame = self.__get_frame()

        import_sprite = pygame.image.load(frame).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, self.scale)

        self.display.blit(resize_sprite, (self.x_axis, self.y_axis))

        self.__enemy_start_level_animation()
        self.__enemy_movement()
        self.rect = resize_sprite.get_rect(topleft=(self.x_axis, self.y_axis))

    def death_animation(self):
        """Method to draw death animation for enemy"""

        frame_1 = "../assets/explosion_one.png"
        frame_2 = "../assets/explosion_two.png"
        frame_3 = "../assets/explosion_three.png"
        frame_4 = "../assets/explosion_four.png"
        frame_5 = "../assets/explosion_five.png"

        frames = [frame_1, frame_2, frame_3, frame_4, frame_5]

        for frame in frames:
            import_sprite = pygame.image.load(frame).convert_alpha()
            sprite = pygame.transform.scale_by(import_sprite, self.scale)
            self.display.blit(sprite, (self.x_axis, self.y_axis))

    def get_enemy_rect(self):
        """Method to return enemy rect"""

        return self.rect

    def __get_frame(self) -> str:
        """Method to get the current frame of the ship"""

        tick = pygame.time.get_ticks()
        frame = self.frame_one

        if tick > self.frame_interval:
            self.state += 1
            self.frame_interval = tick + self.update_interval

            if self.state == 5:
                self.state = 1

        if self.state == 1:
            frame = self.frame_one

        elif self.state == 2:
            frame = self.frame_two

        elif self.state == 3:
            frame = self.frame_three

        elif self.state == 3:
            frame = self.frame_four

        return frame

    def __enemy_start_level_animation(self):
        """Method to animate the enemy to fly onto the screen"""

        if self.y_axis_counter != 0:
            self.y_axis_counter -= 3
            self.y_axis += 3

    def __enemy_movement(self):
        """Method to ensure enemy isn't static"""

        if self.count < 50 and self.count_check is not True:
            self.count += 1
            self.x_axis += 0.2

            if self.count == 50:
                self.count_check = True

        elif self.count > 0 and self.count_check is True:
            self.count -= 1
            self.x_axis -= 0.2

            if self.count == 0:
                self.count_check = False

    ####################
    # WORK IN PROGRESS #
    ####################

    def shoot_laser(self, player, player_object):
        """Method to draw the laser on the screen"""
        laser_check = len(self.laser_coordinates)
        self.__shoot_laser_check(laser_check)
        import_sprite = pygame.image.load(self.laser).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, self.scale)

        if laser_check > 0:
            self.__draw_laser(resize_sprite)
            self.__hit_target(resize_sprite, player, player_object)

    def __shoot_laser_check(self, laser_check: int):
        """Method to determine if laser has been shoot"""

        shoot = random.randrange(0, 50)
        if self.y_axis_counter == 0 and laser_check == 0 and shoot == 25:
            self.laser_coordinates = [self.x_axis + 38, self.y_axis + 75]

    def __draw_laser(self, sprite: pygame.Surface):
        """Method to draw laser"""

        x_axis, y_axis = self.laser_coordinates[0], self.laser_coordinates[1]
        self.display.blit(sprite, (x_axis, y_axis))

    def __hit_target(self, sprite: pygame.Surface, player, player_object):
        """Method which determine if the target has been hit"""

        x_axis, y_axis = self.laser_coordinates[0], self.laser_coordinates[1]
        sprite_rect = sprite.get_rect(topleft=(x_axis, y_axis))
        self.laser_coordinates[1] += 5

        if sprite_rect.colliderect(player):
            player_object.update_heath()
            self.laser_coordinates.clear()

        elif y_axis > 700:
            self.laser_coordinates.clear()
