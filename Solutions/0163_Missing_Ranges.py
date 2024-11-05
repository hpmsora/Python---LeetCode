class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        sol = []

        left = lower
        for each_nums in nums:
            if left <= each_nums - 1:
                sol.append([left, each_nums-1])
                left = each_nums + 1
            else:
                left = each_nums + 1
        if left <= upper:
            sol.append([left, upper])
        return sol