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
        visited = set()
        start = Node(neighbors=[])
        if not node:
            return node
        new_val_dict = {}
        
        # DFS
        def dfs(_node, _new_head):
            head = Node(val=_node.val)
            _new_head.neighbors.append(head)
            visited.add(_node.val)
            new_val_dict[_node.val] = head

            for each_neighbors in _node.neighbors:
                if not each_neighbors.val in visited:
                    dfs(each_neighbors, head)
                else:
                    head.neighbors.append(new_val_dict[each_neighbors.val])
        dfs(node, start)
        
        return start.neighbors[0]