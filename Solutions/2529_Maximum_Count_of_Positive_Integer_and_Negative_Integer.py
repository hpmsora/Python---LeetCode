class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = 0
        pos = 0

        for index, each_nums in enumerate(nums):
            if each_nums < 0:
                neg += 1
            elif each_nums == 0:
                continue
            elif each_nums > 0:
                pos = len(nums) - index
                break
        
        return max(neg, pos)