import pygame

x = pygame.init()
game_window = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")

game_over = False
game_exit = False

while not game_exit:
    for event in pygame.event.get():
        # print(event)  # This will print all the events(motions) occurring while running the game.

        # This will close the game when the user tries to close the program.
        if event.type == pygame.QUIT:
            game_exit = True

        # This will check the pressed key when the user presses the key.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("You have pressed the down arrow key.")

pygame.quit()
quit()
