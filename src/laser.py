import pygame


class laser:
    def __init__(self, display: pygame.Surface):
        self.laser = "../assets/laser.png"
        self.laser_charge = "../assets/laser_charge.png"

        self.display = display
        self.scale = 5

        self.current_laser_charge = 0
        self.laser_charge_axis = 645

        self.manage_lasers = []
        self.manage_lasers_rect = {}

        self.interval = 1000
        self.laser_interval = 0
        self.laser_shoot = False

        self.hit_index = []

    def laser_dict(self, coordinates: tuple[int, int]):
        """Method to to manage bullet state"""

        key = pygame.key.get_pressed()
        tick = pygame.time.get_ticks()

        laser_state = self.laser_interval - tick

        if laser_state > 0:
            self.current_laser_charge = int(50 * round(laser_state / 50) / 50)

        if key[pygame.K_SPACE] and tick > self.laser_interval:
            self.manage_lasers.append(list(coordinates))
            self.laser_interval = tick + self.interval

    def draw_laser(self):
        """Method to draw the laser on the screen"""

        import_sprite = pygame.image.load(self.laser).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, self.scale)

        for count, i in enumerate(self.manage_lasers):
            x_axis = i[0] + 37.5
            y_axis = i[1] - 10

            rect = resize_sprite.get_rect(bottomleft=(x_axis, y_axis))
            self.manage_lasers_rect[count] = rect
            self.display.blit(resize_sprite, (x_axis, y_axis))

    def move_laser(self, enemy: dict):
        """Method to move laser"""

        for count, coordinates in enumerate(self.manage_lasers):
            hit = self.__hit_target(enemy)

            if hit:
                self.manage_lasers.pop(count)
                continue

            coordinates[1] -= 5
            self.manage_lasers[count] = coordinates

            if coordinates[1] <= 45:
                self.manage_lasers.pop(count)

    def draw_laser_charge(self):
        """Method to draw current laser charge"""

        import_sprite = pygame.image.load(self.laser_charge).convert_alpha()
        resize_sprite = pygame.transform.scale_by(import_sprite, self.scale)

        max_laser_charge = 20

        for i in range(max_laser_charge - self.current_laser_charge):
            current = self.laser_charge_axis + (i * 5)
            self.display.blit(resize_sprite, (current, 690))

    def __hit_target(self, enemy) -> bool:
        """Method to determine if target has been hit"""

        hit = False
        laser_rects = self.manage_lasers_rect

        for i in enemy:
            for j in laser_rects:
                if laser_rects[j].colliderect(enemy[i].get_enemy_rect()):
                    enemy[i].death_animation()
                    enemy.pop(i)
                    hit = True
                    break
            if hit:
                break

        return hit
