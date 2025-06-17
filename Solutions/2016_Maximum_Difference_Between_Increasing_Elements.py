class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        left_min = nums[0]

        sol = -1

        for num in nums[1:]:
            if not left_min < num:
                left_min = min(left_min, num)
                continue
            sol = max(sol, num - left_min)

        return sol