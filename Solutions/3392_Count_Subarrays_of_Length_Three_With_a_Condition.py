class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        sol = 0
        index = 2
        while index < len(nums):
            if 2 * (nums[index-2] + nums[index]) == nums[index-1]:
                sol += 1
            index += 1
        
        return sol