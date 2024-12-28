class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # 1. Find k len summation list
        curr_sum = sum(nums[:k])
        sum_list = [curr_sum]
        for first_num_index, each_nums in enumerate(nums[k:]):
            curr_sum += each_nums - nums[first_num_index]
            sum_list.append(curr_sum)
        
        # 2. Left maxima
        left = [0] * len(sum_list)
        max_idx = 0
        for i in range(len(sum_list)):
            if sum_list[i] > sum_list[max_idx]:
                max_idx = i
            left[i] = max_idx
        
        # 3. Right maxima
        right = [0] * len(sum_list)
        max_idx = len(sum_list) - 1
        for i in range(len(sum_list)-1, -1, -1):
            if sum_list[i] >= sum_list[max_idx]:
                max_idx = i
            right[i] = max_idx
        
        # 4. Global maxima
        max_sum = 0
        sol = [-1, -1, -1]
        for mid in range(k, len(sum_list) - k):
            l, r = left[mid-k], right[mid+k]
            curr_sum = sum_list[l] + sum_list[mid] + sum_list[r]
            if curr_sum > max_sum:
                max_sum = curr_sum
                sol = [l, mid, r]
            elif curr_sum == max_sum:
                sol = min(sol, [l, mid, r])
        
        return sol