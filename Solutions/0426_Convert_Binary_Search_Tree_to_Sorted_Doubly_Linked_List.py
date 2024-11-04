"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        node_dict = {}
        node_list = []

        # DFS
        def helper(_root):
            if not _root:
                return
            
            node_dict[_root.val] = _root
            node_list.append(_root.val)

            # Left
            if _root.left:
                helper(_root.left)
            
            # Right
            if _root.right:
                helper(_root.right)

            return

        helper(root)
        node_list.sort()
        prev_node = node_dict[node_list[-1]]
        for each_val in node_list:
            curr_node = node_dict[each_val]
            prev_node.right = curr_node
            curr_node.left = prev_node
            prev_node = curr_node
        
        return node_dict[node_list[0]]