import pygame


class laser:
    def __init__(self, display: pygame.Surface):
        self.laser = "../assets/laser.png"
        self.display = display
        self.scale = 5

        self.manage_lasers = []

        self.interval = 1000
        self.laser_interval = 0
        self.laser_shoot = False

    def laser_dict(self, coordinates: tuple[int, int]):
        """Method to to manage bullet state"""

        key = pygame.key.get_pressed()
        tick = pygame.time.get_ticks()

        if key[pygame.K_SPACE] and tick > self.laser_interval:
            self.manage_lasers.append(list(coordinates))
            self.laser_interval = tick + self.interval

    def draw_laser(self):
        """Method to draw the laser on the screen"""

        import_sprite = pygame.image.load(self.laser).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, self.scale)

        for i in self.manage_lasers:
            x_axis = i[0] + 35
            y_axis = i[1] - 10

            self.display.blit(resize_sprite, (x_axis, y_axis))

    def move_laser(self):
        """Method to move laser"""

        for count, coordinates in enumerate(self.manage_lasers):
            coordinates[1] -= 5
            self.manage_lasers[count] = coordinates

            if coordinates[1] <= 45:
                self.manage_lasers.pop(count)
