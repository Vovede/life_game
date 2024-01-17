import pygame
import random
from copy import deepcopy

RES = WIDTH, HEIGHT = 1600, 900
TILE = 7
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = -1

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

next_field = [[0 for i in range(W)] for j in range(H)]

# current_field = [[1 if i == W // 2 or j == H // 2 else 0 for i in range(W)] for j in range(H)]
current_field = [[random.randint(0, 1) for i in range(W)] for j in range(H)]
# current_field = [[1 if not (i * j) % 22 else 0 for i in range(W)] for j in range(H)]

water_field = [[1 if random.random() > 0.96 else 0 for i in range(W)] for j in range(H)]
food_field = [[1 if random.random() > 0.96 else 0 for i in range(W)] for j in range(H)]


def check_cell(current_field, water_field, food_field, x, y):
    count = 0
    water = False
    food = False
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1
            if water_field[j][i] and food_field[j][i]:
                water = True
                food = True

    if current_field[y][x]:
        count -= 1
        if count == 1 or count == 2 or (water or food):
            return 1
        return 0
    else:
        if count == 3 or (water or food):
            return 1
        return 0


while True:

    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # draw grid
    #[pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    #[pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]

    # draw cells
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if current_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('white'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            if water_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('blue'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            if food_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('sienna'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            next_field[y][x] = check_cell(current_field, water_field, food_field, x, y)

    current_field = deepcopy(next_field)

    print(round(clock.get_fps()))
    pygame.display.flip()
    clock.tick(FPS)
