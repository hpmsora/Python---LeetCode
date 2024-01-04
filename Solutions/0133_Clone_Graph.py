"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        queue = collections.deque([node])
        sol_dict = {
            node.val : Node(val=node.val, neighbors=[])
        }

        while queue:
            n = queue.popleft()
            n_sol = sol_dict[n.val]

            for each_n_neighbors in n.neighbors:
                if not each_n_neighbors.val in sol_dict:
                    sol_dict[each_n_neighbors.val] = Node(val=each_n_neighbors.val, neighbors=[])
                    queue.append(each_n_neighbors)
                
                n_sol.neighbors.append(sol_dict[each_n_neighbors.val])

        return sol_dict[node.val]