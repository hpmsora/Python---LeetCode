class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

        n = len(grid)
        start = (0, 0)
        end = (n-1, n-1)
        if grid[0][0] == 1:
            return -1
        elif start == end:
            return 1

        stack = collections.deque([(start, 1)])
        visited = set()
        visited.add(start)
        while stack:
            curr_pos, step = stack.popleft()
            
            x, y = curr_pos
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < n and not (nx, ny) in visited:
                    if grid[nx][ny] == 1:
                        continue
                    if (nx, ny) == end:
                        return step + 1
                    visited.add((nx, ny))
                    stack.append(((nx, ny), step + 1))
        return -1