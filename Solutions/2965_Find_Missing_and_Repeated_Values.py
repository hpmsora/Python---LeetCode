class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        grid_set = set([*range(1, n**2+1)])

        sol = []
        for each_row in grid:
            for each_element in each_row:
                if each_element in grid_set:
                    grid_set.remove(each_element)
                else:
                    sol.append(each_element)
        sol.append(grid_set.pop())

        return sol