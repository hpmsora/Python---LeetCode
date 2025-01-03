class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        sol = 0

        for each_nums in nums[:-1]:
            left += each_nums
            right -= each_nums
            if left >= right:
                sol += 1
        return sol