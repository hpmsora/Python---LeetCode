class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        max_x = len(grid)
        max_y = len(grid[0])
        curr_cell_x, curr_cell_y = (0, 0)

        for x in range(max_x):
            isFound = False
            for y in range(max_y):
                if grid[x][y] == 1:
                    curr_cell_x, curr_cell_y = (x, y)
                    isFound = True
                    break
            if isFound:
                break

        seen = set()
        seen.add((curr_cell_x, curr_cell_y))

        def helper(_x, _y):
            print(_x, _y)
            sol = 0
            # x + 1, y
            if _x+1 < max_x:
                if grid[_x + 1][_y]==0:
                    sol += 1
                elif not (_x+1, _y) in seen:
                    seen.add((_x+1, _y))
                    sol += helper(_x+1, _y)
            else:
                sol += 1
            # x - 1, y
            if _x-1 >= 0:
                if grid[_x - 1][_y]==0:
                    sol += 1
                elif not (_x-1, _y) in seen:
                    seen.add((_x-1, _y))
                    sol += helper(_x-1, _y)
            else:
                sol += 1
            # x, y + 1
            if _y+1 < max_y:
                if grid[_x][_y+1]==0:
                    sol += 1
                elif not (_x, _y+1) in seen:
                    seen.add((_x, _y+1))
                    sol += helper(_x, _y+1)
            else:
                sol += 1
            # x, y - 1
            if _y-1 >= 0:
                if grid[_x][_y-1]==0:
                    sol += 1
                elif not (_x, _y-1) in seen:
                    seen.add((_x, _y-1))
                    sol += helper(_x, _y-1)
            else:
                sol += 1
            return sol
        return helper(curr_cell_x, curr_cell_y)