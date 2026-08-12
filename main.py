import pygame
import numpy as np
import renderer
import logic

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
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

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        grid = logic.calculate_next_generation(grid)

        renderer.draw_grid(screen, grid, CELL_SIZE)

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()