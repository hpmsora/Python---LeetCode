class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        for each_w_m, each_w_n in walls:
            grid[each_w_m][each_w_n] = -1

        for each_g_m, each_g_n in guards:
            grid[each_g_m][each_g_n] = -1
        
        dirs= [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for each_g_m, each_g_n in guards:

            for dm, dn in dirs:
                new_each_g_m = each_g_m
                new_each_g_n = each_g_n
                while True:
                    new_each_g_m += dm
                    new_each_g_n += dn
                    if new_each_g_m < 0 or new_each_g_m >= m or new_each_g_n < 0 or new_each_g_n >= n or grid[new_each_g_m][new_each_g_n] == -1:
                        break
                    grid[new_each_g_m][new_each_g_n] = -2
            
        return sum(each_m.count(0) for each_m in grid)