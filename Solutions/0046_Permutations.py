class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def helper(_nums, _parent):
            nonlocal sol
            if not _nums:
                sol.append(_parent)
                return
            
            for index, each_nums in enumerate(_nums):
                if 0 == len(_nums) - 1:
                    sol.append(_parent + [each_nums])
                elif index == 0:
                    helper(_nums[1:], _parent + [each_nums])
                else:
                    helper(_nums[:index] + _nums[index+1:], _parent + [each_nums])
        helper(nums, [])
        return sol