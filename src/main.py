#!/bin/python3
import pygame
from game_logic import game_logic

pygame.init()


def main():
    """Main Method"""

    game_logic().main_loop()

    pygame.quit()


if __name__ == "__main__":
    main()
