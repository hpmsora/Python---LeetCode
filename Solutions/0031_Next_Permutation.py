class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 1324 -> 1342
        # 1342 -> 1423

        prev = -1
        new_list = []
        index = len(nums) - 1
        isSwap = False
        while index >= 0:
            num = nums[index]
            if num < prev:
                # Swap first
                diff = float('inf')
                s_index = 0
                for sub_index in range(index+1, len(nums)):
                    sub_num = nums[sub_index]
                    if sub_num > num:
                        if sub_num - num < diff:
                            diff = sub_num - num
                            s_index = sub_index
                temp_num = nums[s_index]
                nums[s_index] = nums[index]
                nums[index] = temp_num
                new_list = nums[index + 1:]
                new_list.sort()
                count = 0
                for sub_index in range(index + 1, len(nums)):
                    nums[sub_index] = new_list[count]
                    count += 1
                nums = nums[:index] + new_list
                isSwap = True
                break
            prev = num
            index -= 1


        if not isSwap:
            nums.sort()