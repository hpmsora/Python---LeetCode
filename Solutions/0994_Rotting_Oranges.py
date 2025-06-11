class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque([])
        
        orange_set = set()
        
        max_x = len(grid)
        max_y = len(grid[0])
        
        for x in range(max_x):
            for y in range(max_y):
                if grid[x][y] == 2:
                    queue.append((x, y, 0))
                elif grid[x][y] == 1:
                    orange_set.add((x, y))
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        sol = 0
        while queue:
            x, y, step = queue.popleft()
            sol = max(sol, step)
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                
                if nx >= 0 and nx < max_x and ny >= 0 and ny < max_y:
                    if (nx, ny) in orange_set:
                        orange_set.remove((nx, ny))
                        queue.append((nx, ny, step + 1))
        if len(orange_set) == 0:
            return sol
        else:
            return -1