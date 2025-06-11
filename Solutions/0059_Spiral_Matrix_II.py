class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        sol = [[0 for _ in range(n)] for _ in range(n)]
        
        index = 1
        queue = collections.deque([(0, 0)])

        while queue:
            if index > n **2:
                break
            x, y = queue.popleft()
            sol[x][y] = index
            nx, ny = x + dirs[0][0], y + dirs[0][1]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and sol[nx][ny] == 0:
                queue.append((nx, ny))
            else:
                d = dirs.pop(0)
                dirs.append(d)
                nx, ny = x + dirs[0][0], y + dirs[0][1]
                queue.append((nx, ny))
            index += 1
        return sol