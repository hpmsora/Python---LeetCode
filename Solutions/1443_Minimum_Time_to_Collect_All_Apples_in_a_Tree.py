class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        isValid = False
        for each_hasApple in hasApple:
            if each_hasApple:
                isValid = True
                break
        if not isValid:
            return 0

        edges_dict = {}

        for index in range(n):
            edges_dict[index] = []

        for start, end in edges:
            edges_dict[start].append(end)
            edges_dict[end].append(start)

        visited = set()

        # DFS
        def dfs(_index):
            visited.add(_index)
            head_sol = 0
            if hasApple[_index]:
                head_sol = 1
            
            child_sol = 0
            if _index in edges_dict:
                for each_index in edges_dict[_index]:
                    if not each_index in visited:
                        child_sol += dfs(each_index)

            if not child_sol == 0:
                return child_sol + 1
            elif not head_sol == 0:
                return 1
            else:
                return 0
        return (dfs(0)-1)*2