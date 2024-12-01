class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 1
        
        prev_num = nums[index]
        index -= 1
        
        while index >= 0:
            each_nums = nums[index]
            
            if prev_num > each_nums:
                index_2 = index + 1
                min_gap = prev_num - each_nums
                next_digit_index = index_2
                while index_2 < len(nums) and nums[index_2] > each_nums:
                    if nums[index_2] - each_nums < min_gap:
                        next_digit_index = index_2
                        min_gap = nums[index_2] - each_nums
                    index_2 += 1
                nums[index], nums[next_digit_index] = nums[next_digit_index], nums[index]
                # nums[index + 1:] reverse
                new_nums = nums[index + 1:]
                new_nums.sort()
                nums[index + 1:] = new_nums
                return
                break
            prev_num = each_nums
            
            index -= 1
        nums.reverse()