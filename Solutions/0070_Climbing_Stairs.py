class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1,2] + [0]*(n-2)

        for index in range(2, n):
            prepre_dp = dp[index-2]
            pre_dp = dp[index-1]

            dp[index] = prepre_dp + pre_dp
        return dp[-1]