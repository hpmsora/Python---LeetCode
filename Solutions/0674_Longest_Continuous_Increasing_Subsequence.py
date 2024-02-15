class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        sol = 0

        cont_len = 1
        prev = nums[0]

        for num in nums[1:]:
            if num > prev:
                cont_len += 1
            else:
                sol = max(sol, cont_len)
                cont_len = 1
            prev = num
        sol = max(sol, cont_len)

        return sol