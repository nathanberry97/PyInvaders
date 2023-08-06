import pygame


class score:
    def __init__(self, screen: pygame.Surface):
        self.NUMBER = {
            "0": "zero",
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine",
        }
        self.screen = screen

    def display_score(self, score: int) -> None:
        """Method to display current score"""

        score_list = list(str(score))

        digit_one = self.__get_digit(score_list, 0, 1)
        digit_two = self.__get_digit(score_list, 1, 2)
        digit_three = self.__get_digit(score_list, 2, 3)
        digit_four = self.__get_digit(score_list, 3, 4)

        self.__draw_sore(digit_one, 245, 10)
        self.__draw_sore(digit_two, 225, 10)
        self.__draw_sore(digit_three, 205, 10)
        self.__draw_sore(digit_four, 185, 10)

    def display_level(self, level: int) -> None:
        """Method to display current level"""

        level_list = list(str(level))

        digit_one = self.__get_digit(level_list, 0, 1)
        digit_two = self.__get_digit(level_list, 1, 2)

        self.__draw_sore(digit_one, 720, 10)
        self.__draw_sore(digit_two, 700, 10)

    def __draw_sore(self, sprite: str, x: int, y: int) -> None:
        """Method to draw score onto the display"""

        score = pygame.image.load(f"../assets/{sprite}.png").convert_alpha()
        resize_sprite = pygame.transform.scale_by(score, 5)

        self.screen.blit(resize_sprite, (x, y))

    def __get_digit(self, score: list[str], index: int, num: int) -> str:
        """Method get the digit for the score"""

        digit = "zero"

        if len(score) > index:
            digit = self.NUMBER[score[-num]]

        return digit
