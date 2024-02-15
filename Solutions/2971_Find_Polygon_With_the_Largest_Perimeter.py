class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        index = len(nums) - 1
        right_num = nums[index]
        left_sum = sum(nums) - right_num

        while left_sum <= right_num:
            index -= 1
            if index < 2:
                return -1
                break
            
            right_num = nums[index]
            left_sum = left_sum - right_num
        return right_num + left_sum