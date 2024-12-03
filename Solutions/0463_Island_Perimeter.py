class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        start = (0, 0)
        # Find land first
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    start = (x, y)
        
        # Find island corners
        stack = collections.deque([start])
        sol = 0
        visited = set()
        visited.add(start)
        while stack:
            x, y = stack.popleft()
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                
                if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 1:
                    if not (nx, ny) in visited:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                else:
                    sol += 1
        return sol