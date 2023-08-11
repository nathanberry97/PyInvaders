import pygame


class menu:
    def __init__(self, screen: pygame.Surface):
        self.state = 0
        self.screen = screen

    def set_state(self) -> None:
        """Method to set the state"""

        key = pygame.key.get_pressed()

        if key[pygame.K_s] and self.state == 0:
            self.state = 1

        elif key[pygame.K_w] and self.state == 1:
            self.state = 0

    def draw_icon(self):
        """Method to draw the menu icon"""

        if self.state == 0:
            self.__draw_icon("start_icon", 330, 395)

        elif self.state == 1:
            self.__draw_icon("exit_icon", 330, 495)

    def get_state(self) -> int:
        """Method to return the state"""

        return self.state

    def __draw_icon(self, icon, x, y) -> None:
        """Method to draw menu icons onto the display"""

        sprite = f"../assets/{icon}.png"
        import_sprite = pygame.image.load(sprite).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, 5)
        self.screen.blit(resize_sprite, (x, y))
