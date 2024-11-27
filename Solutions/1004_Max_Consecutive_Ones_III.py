class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        zero_count = 0
        sol = 0

        while right < len(nums):
            if not nums[right] == 1:
                zero_count += 1
                while zero_count > k:
                    if nums[left] == 0:
                        zero_count -= 1
                    left += 1
            sol = max(sol, right - left + 1)
            right += 1
        return sol