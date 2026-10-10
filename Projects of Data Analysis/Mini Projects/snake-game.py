import pygame
import random
import sys

# Settings
WIDTH = 640
HEIGHT = 480
CELL_SIZE = 20
FPS = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 150, 255)


def draw_grid(surface):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(surface, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, (40, 40, 40), (0, y), (WIDTH, y))


def random_food_position(snake):
    while True:
        x = random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE
        y = random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake:
            return x, y


def show_text(screen, text, size, color, center):
    font = pygame.font.SysFont(None, size)
    label = font.render(text, True, color)
    rect = label.get_rect(center=center)
    screen.blit(label, rect)


def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    snake = [(WIDTH // 2, HEIGHT // 2), (WIDTH // 2 - CELL_SIZE, HEIGHT // 2), (WIDTH // 2 - 2 * CELL_SIZE, HEIGHT // 2)]
    dir_x, dir_y = CELL_SIZE, 0

    food = random_food_position(snake)
    score = 0
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if not game_over:
                    if event.key == pygame.K_UP and dir_y == 0:
                        dir_x, dir_y = 0, -CELL_SIZE
                    elif event.key == pygame.K_DOWN and dir_y == 0:
                        dir_x, dir_y = 0, CELL_SIZE
                    elif event.key == pygame.K_LEFT and dir_x == 0:
                        dir_x, dir_y = -CELL_SIZE, 0
                    elif event.key == pygame.K_RIGHT and dir_x == 0:
                        dir_x, dir_y = CELL_SIZE, 0
                elif game_over and event.key == pygame.K_r:
                    return game_loop()

        if not game_over:
            head_x, head_y = snake[0]
            new_head = (head_x + dir_x, head_y + dir_y)

            if (
                new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake
            ):
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    food = random_food_position(snake)
                else:
                    snake.pop()

        screen.fill(BLACK)
        draw_grid(screen)

        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

        show_text(screen, f'Score: {score}', 32, WHITE, (70, 20))

        if game_over:
            show_text(screen, 'GAME OVER', 72, BLUE, (WIDTH // 2, HEIGHT // 2 - 20))
            show_text(screen, 'Press R to Restart or ESC to Quit', 36, WHITE, (WIDTH // 2, HEIGHT // 2 + 30))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    game_loop()
