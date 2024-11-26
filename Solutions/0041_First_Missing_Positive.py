class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(-1)
        index = 0

        while index < len(nums):
            curr_num = nums[index]
            if curr_num > 0:
                if not curr_num == index:
                    nums[index] = -1
                    while curr_num > 0 and curr_num < len(nums):
                        if not nums[curr_num] > 0 or nums[curr_num] == curr_num:
                            nums[curr_num] = curr_num
                            break
                        new_num = nums[curr_num]
                        nums[curr_num] = curr_num
                        curr_num = new_num
            index += 1
        curr_num = 1

        while curr_num < len(nums):
            if not nums[curr_num] == curr_num:
                return curr_num
            curr_num += 1
        
        return curr_num