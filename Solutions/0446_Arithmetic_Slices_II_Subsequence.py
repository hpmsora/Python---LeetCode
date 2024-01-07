class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0

        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                if diff < -2**31 or diff > 2**31 - 1:
                    continue

                count = dp[j][diff] if diff in dp[j] else 0

                total_count += count
                dp[i][diff] += count + 1

        return total_count