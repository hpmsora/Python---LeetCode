class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) # n row
        n = len(grid[0]) # n column

        # first row update
        for y in range(1, n):
            grid[0][y] += grid[0][y-1]
        
        # first column update
        for x in range(1, m):
            grid[x][0] += grid[x-1][0]

        # rest of cells
        for x in range(1, m):
            for y in range(1, n):
                grid[x][y] += min([grid[x-1][y], grid[x][y-1]])

        return grid[m-1][n-1]