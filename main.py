import pygame

x = pygame.init()  # This line is important as it initialises all the pygame modules.
print(x)  # (x, y) :- x are the successfully initialised modules and y is the opposite of x.
game_window = pygame.display.set_mode((1200, 500))  # This line is important as it creates the game window.
# 1200 and 500 are the width and length of the window respectively.
