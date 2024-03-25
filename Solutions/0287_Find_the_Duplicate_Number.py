class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_freq_set = set()

        for num in nums:
            if num in num_freq_set:
                return num
            else:
                num_freq_set.add(num)