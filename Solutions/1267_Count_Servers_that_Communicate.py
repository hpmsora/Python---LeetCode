class Solution:
    def countServers(self, grid):
        r = len(grid)
        c = len(grid[0])
        rc = [0] * r
        cc = [0] * c
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    rc[i] += 1
                    cc[j] += 1
        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] and (rc[i] > 1 or cc[j] > 1):
                    ans += 1
        return ans