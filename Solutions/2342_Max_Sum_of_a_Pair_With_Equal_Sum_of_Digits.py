class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_dict = {}

        for each_nums in nums:
            digit_sum = 0

            curr_num = each_nums

            while curr_num >= 1:
                digit_sum += curr_num % 10
                curr_num = curr_num // 10
            if digit_sum in sum_dict:
                num_list = sum_dict[digit_sum]
                if len(num_list) == 1:
                    heapq.heappush(sum_dict[digit_sum], each_nums)
                elif num_list[0] < each_nums:
                    heapq.heappushpop(sum_dict[digit_sum], each_nums)
            else:
                heap = [each_nums]
                heapq.heapify(heap)
                sum_dict[digit_sum] = heap

        sol = -1

        for num_list in sum_dict.values():
            if len(num_list) == 2:
                sol = max(sol, num_list[0] + num_list[1])
        
        return sol