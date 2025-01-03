class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        connections = {}
        for index, conn in enumerate(graph):
            connections[index] = conn

        visited = {}
        visited_node = set()
        #visited[0] = True # (index, group(True or False))
        
        for index in range(len(graph)):
            if not index in visited_node:
                stack = collections.deque([(index, True)])
                visited_node.add(index)
            else:
                continue
            while stack:
                curr_node, group = stack.popleft()
                if curr_node in visited:
                    if not group == visited[curr_node]:
                        return False
                    continue
                else:
                    visited[curr_node] = group
                    visited_node.add(curr_node)
                        
                curr_connections = connections[curr_node]
                for each_connections in curr_connections:
                    stack.append((each_connections, not group))
        return True