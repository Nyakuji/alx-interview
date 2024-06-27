#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Function that returns the perimeter
    of the island described in grid"""
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    land_count = 0
    water_count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                land_count += 1
                if i > 0 and grid[i - 1][j] == 1:
                    water_count += 1
                if i < rows - 1 and grid[i + 1][j] == 1:
                    water_count += 1
                if j > 0 and grid[i][j - 1] == 1:
                    water_count += 1
                if j < cols - 1 and grid[i][j + 1] == 1:
                    water_count += 1

    return land_count * 4 - water_count
