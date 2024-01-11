class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+ 1)]
        
        # Start point
        dp[0] = 0

        # Coins validation check
        new_coins = []
        for coin in coins:
            if coin <= amount:
                new_coins.append(coin)
        coins = new_coins

        # DP processing
        for index in range(amount + 1):
            val = dp[index]
            if not val == float('inf'):
                for coin in coins: # Using every steps
                    if index + coin < amount + 1:
                        dp[index + coin] = min([dp[index + coin], val + 1])
        
        # Impossible check
        if dp[-1] == float('inf'):
            return -1

        return dp[-1]