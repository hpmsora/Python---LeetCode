class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1

        for index in range(high+1):
            if index + zero <= high:
                dp[index+zero] = (dp[index+zero] + dp[index]) % (10**9+7)
            if index + one <= high:
                dp[index+one] = (dp[index+one] + dp[index]) % (10**9+7)
        
        sol = 0

        for index in range(low, high+1):
            sol = (sol + dp[index]) % (10**9+7)
        return sol