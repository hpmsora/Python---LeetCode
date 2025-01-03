class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {}

        curr_sum = 0
        sol = 0

        for each_nums in nums:
            if curr_sum in sum_dict:
                sum_dict[curr_sum] += 1
            else:
                sum_dict[curr_sum] = 1
            curr_sum += each_nums
            if curr_sum - k in sum_dict:
                sol += sum_dict[curr_sum - k]
        return sol