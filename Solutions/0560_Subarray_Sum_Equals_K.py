class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        t_sum = 0
        t_sum_dict = {}
        
        sol = 0
        for each_nums in nums:
            if t_sum in t_sum_dict:
                t_sum_dict[t_sum] += 1
            else:
                t_sum_dict[t_sum] = 1
                
            t_sum += each_nums
            
            if t_sum - k in t_sum_dict:
                sol += t_sum_dict[t_sum - k]
        return sol