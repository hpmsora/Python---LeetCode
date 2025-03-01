class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        index = 0
        zero_count = 0
        while index < len(nums)-1:
            if nums[index] == nums[index+1]:
                nums[index] *= 2
                nums[index+1] = 0
            if nums[index] == 0:
                zero_count += 1
                nums.pop(index)
            else:
                index += 1
        return nums + [0] * zero_count