class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        row_1_sum_rest = sum(grid[0])
        row_2_sum_rest = 0

        min_sum = float('inf')
        for index in range(len(grid[0])):
            row_1_sum_rest -= grid[0][index]
            if index > 0:
                row_2_sum_rest += grid[1][index - 1]
            local_min = max(row_1_sum_rest, row_2_sum_rest)
            if min_sum > local_min:
                min_sum = local_min
        return min_sum