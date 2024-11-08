class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_n = len(nums)
        prefix = [1] * len_n
        suffix = [1] * len_n

        index = 1
        while index < len_n:
            prefix[index] = prefix[index-1] * nums[index-1]
            suffix[len_n - index - 1] = suffix[len_n - index] * nums[len_n - index]
            index += 1
        index = 0
        while index < len_n:
            nums[index] = prefix[index] * suffix[index]
            index += 1
        return nums