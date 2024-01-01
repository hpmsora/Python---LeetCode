class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_nums = sum(nums)
        len_nums = len(nums)
        sol = len_nums

        # Special Case
        if sum_nums < target:
            return 0
        elif sum_nums == target:
            return sol
        
        sum_nums = 0
        left_index = 0
        
        # Regular Processing
        for index in range(len_nums):
            num = nums[index]

            if sum_nums < target:
                sum_nums += num
                if sum_nums >= target:
                    sol = min(sol, index - left_index + 1)
            else:
                sum_nums += num
                while sum_nums >= target:
                    sum_nums -= nums[left_index]
                    left_index += 1
                left_index -= 1
                sum_nums += nums[left_index]
                sol = min(sol, index - left_index + 1)
        
        while sum_nums >= target:
            sum_nums -= nums[left_index]
            left_index += 1
        left_index -= 1
        sum_nums += nums[left_index]
        sol = min(sol, index - left_index + 1)
        return sol
