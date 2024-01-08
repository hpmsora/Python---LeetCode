class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_size = len(nums)
        for index1 in range(nums_size):
            for index2 in range(index1 + 1, nums_size):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]
        return []