class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        sol = [set()]

        for num in nums:
            isExist = False
            for each_sol in sol:
                if not num in each_sol:
                    each_sol.add(num)
                    isExist = True
                    break
            if not isExist:
                sol.append(set([num]))
        return [list(x) for x in sol]