class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_dict = {}

        max_num = 0
        max_freq = 0

        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

            if max_freq > num_dict[num]:
                continue
            elif max_freq < num_dict[num]:
                max_freq = num_dict[num]
                max_num = 1
            elif max_freq == num_dict[num]:
                max_num += 1

        return max_num * max_freq