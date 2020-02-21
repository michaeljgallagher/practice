'''
A robot is located at the top-left corner of an m x n grid.
The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid.
Now consider if some obstacles are added to the grids. How many unique paths
would there be?
'''


def unique_paths_with_obstacles(obstacle_grid):
    m, n = len(obstacle_grid), len(obstacle_grid[0])

    if obstacle_grid[0][0] == 1:
        return 0
    
    obstacle_grid[0][0] = 1
    
    for i in range(1, m):
        obstacle_grid[i][0] = int(obstacle_grid[i][0] == 0 and obstacle_grid[i-1][0] == 1)
        
    for j in range(1, n):
        obstacle_grid[0][j] = int(obstacle_grid[0][j] == 0 and obstacle_grid[0][j-1] == 1)
        
    for i in range(1, m):
        for j in range(1, n):
            if obstacle_grid[i][j] == 0:
                obstacle_grid[i][j] = obstacle_grid[i-1][j] + obstacle_grid[i][j-1]
            else:
                obstacle_grid[i][j] = 0
                
    return obstacle_grid[-1][-1]


obstacle_grid = [
                [0,0,0],
                [0,1,0],
                [0,0,0]
                ]
print(unique_paths_with_obstacles(obstacle_grid) == 2)


obstacle_grid = [
                [0,0,0,0,0,0],
                [0,1,0,1,0,1],
                [0,0,0,0,1,0],
                [1,0,0,0,0,0]
                ]
print(unique_paths_with_obstacles(obstacle_grid) == 5)


obstacle_grid = [
                [0,0,0],
                [0,1,0],
                [0,0,0],
                [0,0,1],
                [0,0,0],
                [0,0,0]
                ]
print(unique_paths_with_obstacles(obstacle_grid) == 7)
