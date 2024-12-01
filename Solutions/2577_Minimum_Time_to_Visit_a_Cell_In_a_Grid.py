class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # [(int(step), int(x), int(y)), ...]
        heap = [(0, 0, 0)]
        heapq.heapify(heap)

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set([(0, 0)])
        target = (m-1, n-1)
        # init
        for dx, dy in dirs:
            nx, ny = 0+dx, 0+dy

            if grid[nx][ny] <= 1 and nx >= 0 and nx < m and ny >= 0 and ny < n:
                visited.add(-1)
        if len(visited) == 1:
            return -1

        # Loop
        while heap:
            curr_cell = heapq.heappop(heap)

            step, x, y = curr_cell

            # valid next
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy

                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    if grid[nx][ny] > step + 1:
                        if not (nx, ny) in visited:
                            if (grid[nx][ny] - step) % 2 == 0:
                                new_step = grid[nx][ny] + 1
                            else:
                                new_step = grid[nx][ny]
                            if target == (nx, ny):
                                return new_step

                            heapq.heappush(heap, (new_step, nx, ny))
                            visited.add((nx, ny))
                        continue
                    if target == (nx, ny):
                        return step + 1
                    if not (nx, ny) in visited:
                        heapq.heappush(heap, (step+1, nx, ny))
                        visited.add((nx, ny))
        return -1
            