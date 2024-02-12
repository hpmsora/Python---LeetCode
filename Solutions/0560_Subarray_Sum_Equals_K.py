class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sol = 0

        curr_sum = 0

        sum_dict = {
            0 : 1
            }

        for num in nums:
            curr_sum += num

            if curr_sum - k in sum_dict:
                sol += sum_dict[curr_sum - k]

            if curr_sum in sum_dict:
                sum_dict[curr_sum] += 1
            else:
                sum_dict[curr_sum] = 1
        
        return sol