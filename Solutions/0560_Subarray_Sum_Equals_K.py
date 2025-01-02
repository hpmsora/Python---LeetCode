class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_nums = { 0 : 1}
        total_sum = 0

        sol = 0

        for each_nums in nums:
            total_sum += each_nums
            if total_sum - k in sum_nums:
                sol += sum_nums[total_sum - k]
            
            if total_sum in sum_nums:
                sum_nums[total_sum] += 1
            else:
                sum_nums[total_sum] = 1
        
        return sol