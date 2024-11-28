class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        m = len(grid)
        n = len(grid[0])

        # stack = [(int(x), int(y), int(start point: -1(start), -2(end)))]
        stack = collections.deque([(0, 0, -1), (m-1, n-1, -2)])
        visited = set([(0, 0), (m-1, n-1)])
        obstacle_set = set()

        while stack:
            curr_cell = stack.popleft()
            x, y, start_point = curr_cell
            visited.add(curr_cell)
            curr_cell_status = grid[x][y]

            grid[x][y] = start_point
            # Add valid cell add
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                
                # Validation check
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                    # No removew necessary
                    if start_point + grid[new_x][new_y] == -3:
                        return 0
                    if not (new_x, new_y) in visited:
                        if grid[new_x][new_y] == 0:
                            stack.appendleft((new_x, new_y, start_point))
                        elif grid[new_x][new_y] == 1 and start_point == -1:
                            obstacle_set.add((new_x, new_y, 1))

        stack = collections.deque(list(obstacle_set))
        first_x, first_y, _ = stack[0]
        visited.add((first_x, first_y))
        while stack:
            curr_cell = stack.popleft()

            x, y, step = curr_cell
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy

                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                    if grid[new_x][new_y] == -2:
                        return step
                    if not (new_x, new_y) in visited:
                        if grid[new_x][new_y] == 1:
                            visited.add((new_x, new_y))
                            stack.append((new_x, new_y, step + 1))
                        elif grid[new_x][new_y] == 0:
                            visited.add((new_x, new_y))
                            stack.appendleft((new_x, new_y, step))