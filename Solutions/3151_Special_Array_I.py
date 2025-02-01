class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        sign = 0 if nums[0] % 2 == 0 else 1

        for each_nums in nums[1:]:
            if each_nums % 2 == sign:
                return False
            else:
                sign = each_nums % 2
        return True