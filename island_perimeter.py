'''
You are given a map in form of a two-dimensional integer grid where 1 represents
land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is
completely surrounded by water, and there is exactly one island (i.e., one or
more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water
around the island). One cell is a square with side length 1. The grid is
rectangular, width and height don't exceed 100. Determine the perimeter of the
island.
'''

def island_perimeter(grid):
    perimeter = 0
    m, n = len(grid), len(grid[0])    
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                if not j or not grid[i][j-1]:
                    perimeter += 1
                if not i or not grid[i-1][j]:
                    perimeter += 1
                if j == n-1 or not grid[i][j+1]:
                    perimeter += 1
                if i == m-1 or not grid[i+1][j]:
                    perimeter += 1   
    return perimeter


grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
print(island_perimeter(grid) == 16)
