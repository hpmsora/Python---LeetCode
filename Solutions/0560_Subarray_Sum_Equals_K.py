class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_index_dict = {0 : 1}

        sol = 0
        curr_sum = 0
        for each_nums in nums:
            curr_sum += each_nums

            # k = curr_sum - x
            # x = curr_sum - k
            if curr_sum - k in sum_index_dict:
                sol += sum_index_dict[curr_sum - k]
            
            if curr_sum in sum_index_dict:
                sum_index_dict[curr_sum] += 1
            else:
                sum_index_dict[curr_sum] = 1
        return sol