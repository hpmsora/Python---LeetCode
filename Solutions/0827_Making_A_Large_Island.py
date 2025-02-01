class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Find islands
        m = len(grid)
        n = len(grid[0])

        # Check visited
        visited = set()
        candidates_pos_islandindex_dict = {}

        # Direction list
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Loop variable
        island_index_size_dict = {}
        island_index = 0

        # Solution Variable
        sol = 1

        for x in range(m):
            for y in range(n):
                if (x, y) in visited:
                    continue
                #print((x, y))
                visited.add((x, y))
                if grid[x][y] == 1:
                    stack = collections.deque([(x, y)])
                    temp_surround_visited = set()
                    island_size = 1

                    while stack:
                        cx, cy = stack.popleft()
                        for dx, dy in dirs:
                            nx, ny = cx + dx, cy + dy

                            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                                if grid[nx][ny] == 0 and not (nx, ny) in temp_surround_visited:
                                    if (nx, ny) in candidates_pos_islandindex_dict:
                                        candidates_pos_islandindex_dict[(nx, ny)].append(island_index)
                                    else:
                                        candidates_pos_islandindex_dict[(nx, ny)] = [island_index]
                                    temp_surround_visited.add((nx, ny))
                                if not (nx, ny) in visited:
                                    if grid[nx][ny] == 1:
                                        stack.append((nx, ny))
                                        island_size += 1
                                    visited.add((nx, ny))
                    island_index_size_dict[island_index] = island_size
                    sol = max(sol, island_size)
                    island_index += 1
        # Find the best solution
        for island_list in candidates_pos_islandindex_dict.values():
            comb_size = 1
            for each_island in island_list:
                comb_size += island_index_size_dict[each_island] 
            sol = max(sol, comb_size)
        return sol