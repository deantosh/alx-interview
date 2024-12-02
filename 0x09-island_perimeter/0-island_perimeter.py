#!/usr/bin/python3
"""
Create a function def island_perimeter(grid): that returns the
perimeter of the island described in grid:

 - grid is a list of list of integers:
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally).
    - grid is rectangular, with its width and height not exceeding 100
 - The grid is completely surrounded by water
 - There is only one island (or nothing).
 - The island doesn’t have “lakes” (water inside that isn’t connected
   to the water surrounding the island).
"""


def island_perimeter(grid):
    """Calculate the perimeter of an island"""

    perimeter = 0

    # Handle: grid is None or empty
    if grid is None or len(grid) == 0:
        return perimeter

    # Handle: grid is not a list of lists
    if not isinstance(grid, list) or not all(
            isinstance(row, list) for row in grid):
        return perimeter

    # Get number of grid rows and cells in each row
    len_row = len(grid)
    len_col = len(grid[0])

    for m in range(len_row):
        for n in range(len_col):
            if grid[m][n] == 1:
                # Check on vertical grid cells
                if m == 0 or grid[m - 1][n] == 0:  # Top
                    perimeter += 1
                if m == len_row - 1 or grid[m + 1][n] == 0:  # Bottom
                    perimeter += 1
                if n == 0 or grid[m][n - 1] == 0:  # Left
                    perimeter += 1
                if n == len_col - 1 or grid[m][n + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
