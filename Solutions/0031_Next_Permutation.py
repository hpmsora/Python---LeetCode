class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        prev_num = nums[-1]

        index_1 = len(nums) - 1

        while index_1 >= 0:
            each_nums = nums[index_1]
            if each_nums < prev_num:
                diff = float('inf')
                swap_index = index_1 + 1
                index_2 = len(nums) - 1
                while index_2 > index_1:
                    if nums[index_2] - each_nums > 0 and nums[index_2] - each_nums < diff:
                        swap_index = index_2
                        diff = nums[index_2] - each_nums
                    index_2 -= 1
                # Swap
                nums[index_1], nums[swap_index] = nums[swap_index], nums[index_1]
                # Rest reverse
                left = index_1 + 1
                right = len(nums) - 1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                return
            else:
                prev_num = each_nums
            index_1 -= 1
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1