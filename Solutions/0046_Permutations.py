class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def helper(_nums, _list):
            if not _nums:
                nonlocal sol
                sol.append(_list)
                return
            
            for num in _nums:
                new_nums = _nums[:]
                new_list = _list[:]
                new_nums.remove(num)
                new_list.append(num)

                helper(new_nums, new_list)
        helper(nums, [])
        return sol