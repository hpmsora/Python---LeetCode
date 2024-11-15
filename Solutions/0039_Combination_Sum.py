class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(_sol, _sum, _candidates):
            if _sum == target:
                return [_sol]
            elif _sum > target:
                return []

            each_sol = []
            for index, each_candididates in enumerate(_candidates):
                each_sol += helper(_sol + [each_candididates], _sum + each_candididates, _candidates[index:])

            return each_sol

        return helper([], 0, candidates)