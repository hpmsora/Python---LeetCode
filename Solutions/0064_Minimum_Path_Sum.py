class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) # n row
        n = len(grid[0]) # n column
        dp = [[ -1 for _ in range(n)] for _ in range(m)]

        queue = [[0, 0]]
        queue_set = set()
        queue_set.add((0, 0))

        val = 0
        while queue:
            x, y = queue.pop(0)

            # Update start --------------------------
            # Up side
            up = float('inf')
            if not x == 0:
                up = dp[x - 1][y]

            # Left side
            left = float('inf')
            if not y == 0:
                left = dp[x][y-1]
            elif x == 0: # First cell
                up = 0
                left = 0
            
            val = grid[x][y] + min([up, left])
            dp[x][y] = val 
            # Update end --------------------------

            # Queue add start --------------------------
            # Add down
            if x + 1 < m:
                if not (x+1, y) in queue_set:
                    queue.append((x+1, y))
                    queue_set.add((x+1, y))
            # Add right
            if y + 1 < n:
                if not (x, y + 1) in queue_set:
                    queue.append((x, y + 1))
                    queue_set.add((x, y + 1))
            # Queue add end --------------------------

        return val