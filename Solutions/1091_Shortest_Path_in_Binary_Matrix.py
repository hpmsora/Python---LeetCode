class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        target = (m-1, n-1)

        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        elif m-1 == 0 and n-1 == 0:
            return 1

        stack = collections.deque([(0, 0, 1)])
        visited = set([(0, 0)])

        while stack:
            x, y, step = stack.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if nx >= 0 and nx < m and ny >= 0 and ny < n and not (nx, ny) in visited:
                    if grid[nx][ny] == 1:
                        continue
                    if (nx, ny) == target:
                        return step + 1
                    visited.add((nx, ny))
                    stack.append((nx, ny, step + 1))
        return -1