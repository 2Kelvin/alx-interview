#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Calculates the perimeter of an island"""
    rws = len(grid)
    cols = len(grid[0])
    perim = 0

    for x in range(rws):
        for y in range(cols):
            if grid[x][y] == 1:
                if x == 0 or grid[x-1][y] == 0:
                    perim += 1
                if x == rws-1 or grid[x+1][y] == 0:
                    perim += 1
                if y == 0 or grid[x][y-1] == 0:
                    perim += 1
                if y == cols-1 or grid[x][y+1] == 0:
                    perim += 1
    return perim
