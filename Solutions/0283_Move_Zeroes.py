class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        new_index = 0

        while index < len(nums):
            num = nums[index]
            if num == 0:
                index += 1
            else:
                nums[new_index] = num
                index += 1
                new_index += 1
        
        while new_index < len(nums):
            nums[new_index] = 0
            new_index += 1