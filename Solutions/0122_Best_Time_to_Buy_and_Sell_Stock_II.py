class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0

        min_p = prices.pop(0)
        prev = min_p
        price = prev
        for price in prices:
            if price > prev:
                if min_p > price:
                    min_p = price
            else:
                sol += prev - min_p
                min_p = price
            prev = price
        if min_p < price:
            sol += prev - min_p
        return sol