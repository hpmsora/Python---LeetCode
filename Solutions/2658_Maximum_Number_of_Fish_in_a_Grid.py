class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()
        sol = 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_x, max_y = len(grid), len(grid[0])

        for index_row, each_row in enumerate(grid):
            for index_col, each_col in enumerate(each_row):
                if (index_row, index_col) in visited or each_col == 0:
                    continue
                stack = collections.deque([(index_row, index_col)])
                curr_fishes = 0
                visited.add((index_row, index_col))
                while stack:
                    x, y = stack.popleft()
                    curr_fishes += grid[x][y]

                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx and nx < max_x and 0 <= ny and ny < max_y:
                            if (nx, ny) in visited:
                                continue
                            else:
                                visited.add((nx, ny))
                            if not grid[nx][ny] == 0:
                                stack.append((nx, ny))
                sol = max(sol, curr_fishes)
        return sol