"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    # DFS
    def helper(self, _root):
        if not _root:
            return
        # Left
        self.helper(_root.left)
        # Update node list
        self.node_list.append(_root)
        # Right
        self.helper(_root.right)
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        self.node_list = []
        
        self.helper(root)

        for index in range(len(self.node_list) - 1):
            self.node_list[index+1].left = self.node_list[index]
            self.node_list[index].right = self.node_list[index+1]
        
        self.node_list[0].left = self.node_list[-1]
        self.node_list[-1].right = self.node_list[0]

        for each_node_list in self.node_list:
            print(each_node_list.left.val)

        return self.node_list[0]