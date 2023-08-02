import pygame


class player:
    def __init__(self, display: pygame.Surface):
        self.display = display

        self.ship_one = "../assets/spaceship_one.png"
        self.ship_two = "../assets/spaceship_two.png"
        self.ship_three = "../assets/spaceship_three.png"

        self.scale = 5
        self.x_axis = 350
        self.y_axis = 550

        self.state = 1
        self.interval = 75
        self.frame_interval = 0
        self.test = 75

    def draw_player(self):
        """Method to draw the player on the screen"""

        frame = self.get_frame()

        import_sprite = pygame.image.load(frame).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, self.scale)

        self.display.blit(resize_sprite, (self.x_axis, self.y_axis))

    def get_frame(self) -> str:
        """Method to get the current frame of the ship"""

        tick = pygame.time.get_ticks()
        frame = self.ship_one

        if tick > self.frame_interval:
            self.state += 1
            self.frame_interval = tick + self.interval
            if self.state == 4:
                self.state = 1

        if self.state == 1:
            frame = self.ship_one

        elif self.state == 2:
            frame = self.ship_two

        elif self.state == 3:
            frame = self.ship_three

        return frame

    def move_player(self):
        """Method to move the player"""

        key = pygame.key.get_pressed()

        if key[pygame.K_a] and self.x_axis >= 55:
            self.x_axis -= 4

        elif key[pygame.K_d] and self.x_axis <= 665:
            self.x_axis += 4

    def get_coordinates(self) -> tuple[int, int]:
        """Method to return the current player coorfinates"""

        return self.x_axis, self.y_axis
