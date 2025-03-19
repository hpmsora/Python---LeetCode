class Solution:
    def minOperations(self, nums):
        n = len(nums)
        k = 0

        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                k += 1

        return -1 if 0 in nums else k