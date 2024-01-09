class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        for i in range(len(nums)):
            i_num = nums[i]
            if target - i_num in nums_set:
                for j in range(i+1, len(nums)):
                    j_num = nums[j]
                    if i_num + j_num == target:
                        return [i, j]