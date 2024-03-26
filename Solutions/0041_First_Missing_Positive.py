class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        index = 0
        len_nums = len(nums)

        while index < len_nums:
            if nums[index] <= 0:
                nums[index] = len_nums + 1
            index += 1
        
        index = 0
        while index < len_nums:
            num = nums[index]
            if abs(num) - 1 < len_nums and abs(num) - 1 >= 0:
                if nums[abs(num) - 1] > 0:
                    nums[abs(num) - 1] = nums[abs(num) - 1] * -1
            index += 1
        
        index = 0
        while index < len_nums:
            if nums[index] > 0:
                return index + 1
            index += 1
        return index + 1