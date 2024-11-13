class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        right = 0
        sum_index_dict = {0:1}
        curr_sum = 0
        
        sol = 0
        
        while right < len(nums):
            curr_sum += nums[right]
            
            diff = curr_sum - k
            
            if diff in sum_index_dict:
                sol += sum_index_dict[diff]
            
            if curr_sum in sum_index_dict:
                sum_index_dict[curr_sum] += 1
            else:
                sum_index_dict[curr_sum] = 1
            right += 1
        return sol