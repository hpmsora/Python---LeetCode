class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        sol_dict = {}
        max_xy = 0

        for x, row in enumerate(nums):
            for y, num in enumerate(row):
                xy = x+y
                if xy in sol_dict:
                    sol_dict[xy] += [num]
                else:
                    sol_dict[xy] = [num]
                max_xy = max(max_xy, xy)
        
        sol = []
        for each_xy in range(max_xy+1):
            if each_xy in sol_dict:
                temp_sol = sol_dict[each_xy]
                temp_sol.reverse()
                sol += temp_sol
        return sol
