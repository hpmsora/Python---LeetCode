class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [ 0 for _ in range(len(nums))]
        dp[0] = nums[0]

        for index in range(1, len(nums)):
            prev = dp[:index-1]
            if prev:
                dp[index] = nums[index] + max(dp[:index - 1])
            else:
                dp[index] = nums[index]

        return max(dp[-2:])