class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        prev_nums = nums[-1]

        index = len(nums) - 1
        isLast = True
        while index >= 0:
            each_nums = nums[index]

            if prev_nums <= each_nums:
                prev_nums = each_nums
            else:
                isLast = False
                next_num = nums[-1]
                next_index = len(nums) - 1
                diff = float('inf')
                for index_2, each_nums2 in enumerate(nums[:index:-1]):
                    index_2 = len(nums) - index_2 - 1
                    if each_nums2 - each_nums > 0 and diff > each_nums2 - each_nums:
                        diff = next_num - each_nums2
                        next_num = each_nums2
                        next_index = index_2
                # Swap
                nums[index] = nums[next_index]
                nums[next_index] = each_nums
                nums[index+1:] = sorted(nums[index+1:])
                break
            index -= 1
        if isLast:
            nums.sort()