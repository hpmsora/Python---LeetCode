class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        stack = collections.deque([])

        max_x = len(isWater)
        max_y = len(isWater[0])

        sol = [ [0 for _ in isWater[0]] for _ in isWater]

        visited = set()

        for index_row, row in enumerate(isWater):
            for index_col, col in enumerate(row):
                if col == 1:
                    stack.append((index_row, index_col, 0))
                    visited.add((index_row, index_col))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while stack:
            row, col, height = stack.popleft()
            sol[row][col] = height

            for dx, dy in dirs:
                nx, ny = row + dx, col + dy
                if nx >= 0 and nx < max_x and ny >= 0 and ny < max_y and not (nx, ny) in visited:
                    stack.append((nx, ny, height + 1))
                    visited.add((nx, ny))
        return sol