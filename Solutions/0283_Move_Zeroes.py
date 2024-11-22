class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        max_right_index = len(nums) - 1
        
        while index < len(nums) and index <= max_right_index:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                max_right_index -= 1
            else:
                index += 1