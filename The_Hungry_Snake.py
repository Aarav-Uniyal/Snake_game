import pygame
import random
import os

init = pygame.init()
pygame.mixer.init()
screen_width = 700
screen_height = 500
fps = 30
clock = pygame.time.Clock()
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Hungry Snake")
background = pygame.image.load("snake.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height)).convert_alpha()
font = pygame.font.SysFont(None, 35)


def plot_snake(window, colour, lst, size):
    for x, y in lst:
        pygame.draw.rect(window, colour, [x, y, size, size])


def display_text(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    game_window.blit(screen_text, [x, y])


def welcome():
    pygame.mixer.music.load("back.mp3")
    pygame.mixer.music.play(-1)
    purple = (218, 112, 214)
    black = (0, 0, 0)
    exit_game = False
    while not exit_game:
        game_window.fill(purple)
        display_text("Welcome To \'The Hungry Snake\'!", black, 120, 200)
        display_text("Press \'Space bar\' to play.", black, 160, 250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    game_loop()

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


def game_loop():
    game_over = False
    game_exit = False
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (144, 238, 144)
    snake_x = 100
    snake_y = 100
    snake_size = 15
    velocity_x = 0
    velocity_y = 0
    normal_velocity = 5
    score = 0
    snake_list = []
    snake_length = 1
    food_x = random.randint(20, round(screen_width / 2))
    food_y = random.randint(20, round(screen_height / 2))

    if not os.path.exists("hi-score.txt"):
        with open("hi-score.txt", "w") as f:
            f.write("0")

    with open("hi-score.txt", "r") as f:
        high_score = f.read()

    pygame.mixer.music.load("play.mp3")
    pygame.mixer.music.play(-1)
    while not game_exit:
        if game_over:
            with open("hi-score.txt", "w") as f:
                f.write(str(high_score))

            game_window.fill(green)
            display_text("GAME OVER! Press \'Enter\' to continue.", red, 100, 200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = normal_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -normal_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -normal_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = normal_velocity
                        velocity_x = 0

                    if event.key == pygame.K_s:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 10
                if score > int(high_score):
                    high_score = score

                food_x = random.randint(20, round(screen_width / 2))
                food_y = random.randint(20, round(screen_height / 2))
                snake_length += 5

            game_window.fill(green)
            game_window.blit(background, (0, 0))
            head = [snake_x, snake_y]
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load("Crash.mp3")
                pygame.mixer.music.play()

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load("Crash.mp3")
                pygame.mixer.music.play()

            plot_snake(game_window, blue, snake_list, snake_size)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])
            display_text("Score: " + str(score) + "  Hi-score: " + str(high_score), red, 5, 5)

        clock.tick(fps)
        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == '__main__':
    welcome()
