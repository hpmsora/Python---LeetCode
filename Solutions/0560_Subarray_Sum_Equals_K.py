class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_stack_dict = {}
        
        sol = 0
        
        t_sum = 0
        for each_nums in nums:
            #if each_nums == k:
            #    sol += 1
            if each_nums + t_sum == k:
                sol += 1
                
            if t_sum - k + each_nums in sum_stack_dict:
                # t_sum - ? + each_nums = k
                sol += sum_stack_dict[t_sum - k + each_nums]
            
            t_sum += each_nums
            
            if t_sum in sum_stack_dict:
                sum_stack_dict[t_sum] += 1
            else:
                sum_stack_dict[t_sum] = 1

        return sol