import time
import os
import random

def create_grid(rows, cols):
    """Generates a random starting grid of alive (1) and dead (0) cells."""
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    """Renders the grid cleanly in the terminal using visual anchors."""
    os('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print("".join("█" if cell else " " for cell in row))

def get_neighbors(grid, r, c, rows, cols):
    """Counts the 8 surrounding active cells using a toroidal (wrapping) grid."""
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            # The modulo % operator forces coordinates to wrap around boundaries
            count += grid[(r + i) % rows][c + j % cols]
    return count

def update_grid(grid, rows, cols):
    """Applies Conway's rules to calculate the next step of evolution."""
    new_grid = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            neighbors = get_neighbors(grid, r, c, rows, cols)
            if grid[r][c] == 1 and neighbors in [2, 3]:
                new_grid[r][c] = 1  # Survival
            elif grid[r][c] == 0 and neighbors == 3:
                new_grid[r][c] = 1  # Birth
    return new_grid

def run_simulation(rows=20, cols=40, generations=50):
    """Runs the main infinite loop of life."""
    grid = create_grid(rows, cols)
    for _ in range(generations):
        print_grid(grid)
        grid = update_grid(grid, rows, cols)
        time.sleep(0.1)

if __name__ == "__main__":
    run_simulation()
