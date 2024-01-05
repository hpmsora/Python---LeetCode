class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size_nums = len(nums)
        dp = [1]*size_nums
        sol = 1

        for i in range(size_nums):
            num = nums[i]
            for j in range(i):
                if nums[j] < num:
                    dp[i] = max(dp[i], dp[j] + 1)
                    sol = max(dp[i], sol)
        return sol