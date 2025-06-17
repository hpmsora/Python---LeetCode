class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        sol = 0
        visited = set()

        max_x = len(grid)
        max_y = len(grid[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x in range(max_x):
            for y in range(max_y):
                if (x, y) in visited:
                    continue
                visited.add((x, y))

                if grid[x][y] == "1":
                    queue = collections.deque([(x, y)])
                    while queue:
                        cx, cy = queue.popleft()
                        for dx, dy in dirs:
                            nx, ny = cx + dx, cy + dy
                            if nx >= 0 and nx < max_x and ny >= 0 and ny < max_y and not (nx, ny) in visited:
                                if grid[nx][ny] == "1":
                                    queue.append((nx, ny))
                                visited.add((nx, ny))
                    sol += 1
        return sol