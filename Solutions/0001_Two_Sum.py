class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_dict = {}
        for index, each_nums in enumerate(nums):
            if target-each_nums in num_index_dict:
                return [num_index_dict[target-each_nums], index]
            num_index_dict[each_nums] = index