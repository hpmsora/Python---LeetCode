class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_sum = 0
        prev_num = 0
        sol = 0

        for each_nums in nums:
            if prev_num < each_nums:
                curr_sum += each_nums
            else:
                sol = max(curr_sum, sol)
                curr_sum = each_nums
            prev_num = each_nums

        return max(curr_sum, sol)