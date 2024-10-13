class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        sol_range = float('inf')
        sol = [0,0]

        pop_list = []
        pop_list_max = -float('inf')

        # init pop_list
        for index, each_nums in enumerate(nums):
            new_num = each_nums.pop(0)
            heapq.heappush(pop_list, (new_num, index))
            if new_num > pop_list_max:
                pop_list_max = new_num

        if len(pop_list) == 1:
            num, index = heapq.heappop(pop_list)
            return [num, num]

        while nums:
            min_num, min_index = heapq.heappop(pop_list)

            if sol_range > pop_list_max-min_num:
                sol_range = pop_list_max-min_num
                sol = [min_num, pop_list_max]

            if not nums[min_index]:
                return sol
            else:
                new_num = nums[min_index].pop(0)
                heapq.heappush(pop_list,(new_num, min_index))
                if new_num > pop_list_max:
                    pop_list_max = new_num
        return [min_num, pop_list_max]