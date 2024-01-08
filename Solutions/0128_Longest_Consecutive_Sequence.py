class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_len = 0
        nums_len_dict = {}

        for num in nums_set:
            num_len = 1

            num_temp = num
            while num_temp - 1 in nums_set:
                num_temp -= 1
                if num_temp in nums_len_dict:
                    num_len += nums_len_dict[num_temp]
                    break
                num_len += 1
            
            if num_len > 1:
                nums_len_dict[num] = num_len

            if max_len < num_len:
                max_len = num_len
        return max_len