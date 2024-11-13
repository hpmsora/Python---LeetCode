class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        zero_count = 0
        while index < len(nums):
            if nums[index] == 0:
                nums.pop(index)
                zero_count += 1
            else:
                index += 1
        
        nums += [0] * zero_count