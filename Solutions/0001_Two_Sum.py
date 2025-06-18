class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_dict = {}

        for index, num in enumerate(nums):
            if target - num in num_index_dict:
                return [num_index_dict[target - num], index]
            else:
                num_index_dict[num] = index