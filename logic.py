import numpy as np

def calculate_next_generation(grid):

    rows = len(grid)
    cols = len(grid[0])

    next_grid = np.zeros((rows, cols))

    for row in range(rows):
        for col in range(cols):

            alive_neighbors = 0

            for i in range(-1, 2):
                for j in range(-1, 2):

                    if i == 0 and j == 0:
                        continue

                    neighbor_row = (row + i) % rows
                    neighbor_col = (col + j) % cols

                    alive_neighbors += grid[neighbor_row][neighbor_col]

            current_state = grid[row][col]

            if current_state == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                next_grid[row][col] = 0
            elif current_state == 0 and alive_neighbors == 3:
                next_grid[row][col] = 1
            else:
                next_grid[row][col] = current_state

    return next_grid