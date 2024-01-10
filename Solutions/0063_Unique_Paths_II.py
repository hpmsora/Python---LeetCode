class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) # n row
        n = len(obstacleGrid[0]) # n column

        # first element update
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            obstacleGrid[0][0] = -1

        # first row update
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                obstacleGrid[0][j] = 0
            else:
                if obstacleGrid[0][j-1] == 0:
                    obstacleGrid[0][j] = 0
                else:
                    obstacleGrid[0][j] = -1
        
        # first column update
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
            else:
                if obstacleGrid[i-1][0] == 0:
                    obstacleGrid[i][0] = 0
                else:
                    obstacleGrid[i][0] = -1
        
        # rest of cells
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        
        return obstacleGrid[m-1][n-1] * -1