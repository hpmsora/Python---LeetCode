class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        sol = []

        # Empty Case
        if not nums:
            return [[lower, upper]]

        # Loop
        for num in nums:
            if lower == num: # Case 1: lower bound == current num
                lower = num + 1
            elif lower < num and num <= upper: # Case 2: lower < current num < upper
                sol.append([lower, num - 1])
                lower = num + 1
            else: # out of upper bound
                break

        # Last bound check
        if lower <= upper:
            sol.append([lower, upper])
        
        return sol