class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0

        min_p = prices[0]

        for price in prices:
            if price < min_p:
                min_p = price
            sol = max(sol, price - min_p)

        return sol