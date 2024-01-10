class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()

        direction = 0 # 0:right; 1:down; 2:left; 3:up
        count = 0

        m = len(matrix) # n row
        n = len(matrix[0]) # n column

        cell = (0, 0)
        sol = []

        # x: row index
        # y: column index
        while count < m*n:
            visited.add(cell)
            x, y = cell
            print(cell)
            sol.append(matrix[x][y])

            if direction == 0: # right
                if y + 1 > n - 1 or (x, y+1) in visited:
                    cell = (x+1, y) # change to down
                    direction = 1
                else:
                    cell = (x, y+1)
            elif direction == 1: # down
                if x + 1 > m - 1 or (x + 1, y) in visited:
                    cell = (x, y - 1) # change to left
                    direction = 2
                else:
                    cell = (x+1, y)
            elif direction == 2: # left
                if y == 0 or (x, y - 1) in visited:
                    cell = (x-1, y) # change to up
                    direction = 3
                else:
                    cell = (x, y-1)
            else: # up
                if (x-1, y) in visited:
                    cell = (x, y+1) # change to right
                    direction = 0
                else:
                    cell = (x-1, y)
            count += 1
        return sol