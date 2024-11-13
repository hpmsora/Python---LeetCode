class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        index = len(nums) - 1
        isSol = False
        while index >= 1:
            prev_num = nums[index-1]
            curr_num = nums[index]
            
            if prev_num < curr_num:
                min_diff_index = 0
                min_diff = float('inf')
                for index_2, each_nums in enumerate(nums[index:]):
                    if each_nums > prev_num:
                        diff = each_nums - prev_num
                        if diff < min_diff:
                            min_diff = diff
                            min_diff_index = index_2 + index
                temp_num = prev_num
                nums[index-1] = nums[min_diff_index]
                nums[min_diff_index] = temp_num
                nums[index:] = sorted(nums[index:])
                isSol = True
                break
            
            index -= 1
        if not isSol:
            nums.sort()