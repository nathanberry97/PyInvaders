import pygame


class player:
    def __init__(self, display: pygame.Surface):
        self.display = display
        self.ship = "../assets/spaceship.png"
        self.scale = 5
        self.x_axis = 350
        self.y_axis = 550

    def draw_player(self):
        """Method to draw the player on the screen"""

        import_sprite = pygame.image.load(self.ship).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, self.scale)

        self.display.blit(resize_sprite, (self.x_axis, self.y_axis))

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
