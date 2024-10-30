class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # [(x, y, dis)]
        dp = [(0, 0, 1)]

        wid = len(grid)
        hei = len(grid[0])

        target = (wid-1, hei-1)

        visited = set()
        visited.add((0, 0))

        if grid[0][0] == 1:
            return -1

        while dp:
            x, y, dis = dp.pop(0)

            if (x, y) == target:
                return dis
            
            # x + 1
            if x + 1 < wid:
                if (not (x+1, y) in visited) and (grid[x+1][y] == 0):
                    dp.append((x + 1, y, dis + 1))
                    visited.add((x+1, y))
                if y + 1 < hei:
                    if (not (x+1, y+1) in visited) and (grid[x+1][y+1] == 0):
                        dp.append((x+1, y+1, dis + 1))
                        visited.add((x+1, y+1))
            # y + 1
            if y + 1 < hei:
                if (not (x, y+1) in visited) and (grid[x][y+1] == 0):
                    dp.append((x, y+1, dis + 1))
                    visited.add((x, y+1))
                if x - 1 >= 0:
                    if (not (x-1, y+1) in visited) and (grid[x-1][y+1] == 0):
                        dp.append((x-1, y+1, dis + 1))
                        visited.add((x-1, y+1))
            # x - 1
            if x - 1 >= 0:
                if (not (x-1, y) in visited) and (grid[x-1][y] == 0):
                    dp.append((x-1, y, dis + 1))
                    visited.add((x-1, y))
                if y - 1 >= 0:
                    if (not (x-1, y-1) in visited) and (grid[x-1][y-1] == 0):
                        dp.append((x-1, y-1, dis + 1))
                        visited.add((x-1, y-1))
            # y - 1
            if y - 1 >= 0:
                if (not (x, y-1) in visited) and (grid[x][y-1] == 0):
                    dp.append((x, y-1, dis + 1))
                    visited.add((x, y-1))
                if x + 1 < hei:
                    if (not (x+1, y-1) in visited) and (grid[x+1][y-1] == 0):
                        dp.append((x+1, y-1, dis + 1))
                        visited.add((x+1, y-1))
        return -1