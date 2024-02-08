class Solution:
    def numSquares(self, n: int) -> int:
        square_root_list = []

        for i in range(1,n + 1):
            i_sqr = i**2
            if i_sqr <= n:
                square_root_list.append(i_sqr)
        
        dp = [100000 for _ in range(n + 1)]
        dp[0] = 0

        for index in range(len(dp)):
            curr_count = dp[index]
            for poss_num in square_root_list:
                if index + poss_num < len(dp):
                    dp[index + poss_num] = min(dp[index + poss_num], curr_count + 1)
                else:
                    break
        return dp[-1]