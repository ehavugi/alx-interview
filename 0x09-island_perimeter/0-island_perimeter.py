#!/usr/bin/python3
"""island parameter module
"""


def island_perimeter(grid):
    """given a grid with one island fully enclosed, without internal lakes.
    1. represent land, 0 represent water. cells horizontall/vertically
        connected(not diagonally)
    2. grid is rectangular, with its width and height not exceeding 100
    3. gridd is completely surrounded by water
    4. there is one island (or nothing)
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Assume 4 sides

                # check for adjacent land cells and substract from perimeter
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col-1] == 1:
                    perimeter -= 2
    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
        ]
    print(island_perimeter(grid))  # 2
