class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_dict = {}
        blue_dict = {}
        
        for x, y in redEdges:
            if x in red_dict:
                red_dict[x].append(y)
            else:
                red_dict[x] =[y]
        for x, y in blueEdges:
            if x in blue_dict:
                blue_dict[x].append(y)
            else:
                blue_dict[x] =[y]
            
        sol = []
        
        # r: -1
        # b: 1
        for z in range(n):
            # red start
            z_sol_r = float('inf')
            queue = collections.deque([(0, -1, 0)])
            visited = set()
            visited.add((0, -1))
            while queue:
                curr, next_color, steps = queue.popleft()
                if curr == z:
                    z_sol_r = steps
                    break
                next_nodes = []
                if next_color == -1 and curr in red_dict:
                        next_nodes = red_dict[curr]
                elif next_color == 1 and curr in blue_dict:
                    next_nodes = blue_dict[curr]
                for each_next_nodes in next_nodes:
                    if (each_next_nodes, next_color * -1) in visited:
                        continue
                    visited.add((each_next_nodes, next_color * -1))
                    queue.append((each_next_nodes, next_color * -1, steps + 1))
            # blue start
            z_sol_b = float('inf')
            queue = collections.deque([(0, 1, 0)])
            visited = set()
            visited.add((0, 1))
            while queue:
                curr, next_color, steps = queue.popleft()
                if curr == z:
                    z_sol_b = steps
                    break
                next_nodes = []
                if next_color == -1 and curr in red_dict:
                        next_nodes = red_dict[curr]
                elif next_color == 1 and curr in blue_dict:
                    next_nodes = blue_dict[curr]
                for each_next_nodes in next_nodes:
                    if (each_next_nodes, next_color * -1) in visited:
                        continue
                    visited.add((each_next_nodes, next_color * -1))
                    queue.append((each_next_nodes, next_color * -1, steps + 1))
            z_sol = min(z_sol_r, z_sol_b)
            if z_sol == float('inf'):
                sol.append(-1)
            else:
                sol.append(z_sol)
            
        return sol