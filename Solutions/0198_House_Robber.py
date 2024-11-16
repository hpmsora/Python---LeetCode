class Solution:
    def rob(self, nums: List[int]) -> int:
        index = 0

        max_value = 0

        while index < len(nums):
            if index == 0:
                max_value = nums[index]
            elif index == 1:
                max_value = max(max_value, nums[index])
                nums[index] = max_value
            elif index == 2:
                max_value = max(max_value, nums[index] + nums[index-2])
                nums[index] = max_value
            else:
                max_value = max(max_value, nums[index]+ nums[index-2], nums[index]+nums[index-3])
                nums[index] = max_value
            index += 1
        return max_value