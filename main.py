from operator import truediv

import pygame
import numpy as np
import renderer
import logic

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 5
FPS = 60

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()

    rows = SCREEN_HEIGHT // CELL_SIZE
    cols = SCREEN_WIDTH // CELL_SIZE

    grid = np.random.choice([0, 1], size=(rows, cols), p=[0.8, 0.2])

    running = True
    paused = False
    space_down = False

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:

            if not space_down:
                space_down = True
                paused = not paused

        elif space_down:
            space_down = False

        if not paused:
            grid = logic.calculate_next_generation(grid)

        renderer.draw_grid(screen, grid, CELL_SIZE)

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()