class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        prev = nums[-1]
        sol = 0

        for num in nums:
            sol = max(sol, abs(prev - num))
            prev = num
        return sol