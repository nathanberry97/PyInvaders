import pygame


class enemy:
    def __init__(self, display: pygame.Surface, x_axis: int, y_axis: int):
        self.display = display

        self.count = 0
        self.count_check = False

        self.y_axis_counter = 450

        self.x_axis = x_axis
        self.y_axis = y_axis - self.y_axis_counter
        self.scale = 5

        self.frame_one = "../assets/alien_one.png"
        self.frame_two = "../assets/alien_two.png"
        self.frame_three = "../assets/alien_three.png"
        self.frame_four = "../assets/alien_four.png"

        self.state = 1
        self.update_interval = 100
        self.frame_interval = 0

    def draw_enemy(self):
        """Method to draw the player on the screen"""

        frame = self.__get_frame()

        import_sprite = pygame.image.load(frame).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, self.scale)

        self.display.blit(resize_sprite, (self.x_axis, self.y_axis))

        self.__enemy_start_level_animation()
        self.__enemy_movement()

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

    def get_coordinates(self):
        """Method to return the current coordinates"""

        return self.x_axis, self.y_axis

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
