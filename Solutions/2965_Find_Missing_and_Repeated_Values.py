class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        num_set = set()
        n = len(grid) ** 2
        grid_sum = n * (n + 1) / 2

        curr_sum = 0

        sol = []

        for each_row in grid:
            for each_num in each_row:
                curr_sum += each_num
                if each_num in num_set:
                    sol.append(each_num)
                else:
                    num_set.add(each_num)

        sol.append(int(grid_sum - curr_sum + sol[0]))

        return sol