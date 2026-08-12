import pygame

BACKGROUND_COLOR = (0, 0, 0)
ALIVE_COLOR = (0, 153, 0)

def draw_grid(screen, grid, cell_size):

    screen.fill(BACKGROUND_COLOR)

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):

            if grid[row][col] == 1:

                x_pos = col * cell_size
                y_pos = row * cell_size

                cell_rect = (x_pos, y_pos, cell_size - 1, cell_size - 1)

                pygame.draw.rect(screen, ALIVE_COLOR, cell_rect)

    pygame.display.flip()