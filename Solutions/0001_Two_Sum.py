class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for index, each_nums in enumerate(nums):
            if target - each_nums in nums_dict:
                return [index, nums_dict[target-each_nums]]
            nums_dict[each_nums] = index