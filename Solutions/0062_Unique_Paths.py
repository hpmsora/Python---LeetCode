class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [([0] * n) for i in range(m)]
        dp[0][0] = 1

        # Small matrix check
        if m > 1:
            if n > 1:
                look_up_list = [(1,0), (0,1)]
            else:
                look_up_list = [(1,0)]
        elif n > 1:
            look_up_list = [(0, 1)]
        else:
            return 1
        
        # Investigate all dp
        while look_up_list:
            x, y = look_up_list.pop(0)
            if dp[x][y] == 0:
                if x == 0:
                    dp[x][y] = dp[x][y-1]
                elif y == 0:
                    dp[x][y] = dp[x-1][y]
                else:
                    dp[x][y] = dp[x][y-1] + dp[x-1][y]
                if (x == m - 1) and (y == n - 1):
                    return dp[x][y]
                if x == m - 1:
                    look_up_list.append((x, y + 1))
                elif y == n - 1:
                    look_up_list.append((x + 1, y))
                else:
                    look_up_list.append((x + 1, y))
                    look_up_list.append((x, y + 1))