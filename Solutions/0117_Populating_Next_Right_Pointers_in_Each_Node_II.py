"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        dp = [(root, 0)]

        dummy_node = Node(left=root)

        while dp:
            curr_node, curr_level = dp.pop(0)
            if not dp:
                curr_node.next = None
            else:
                next_node, next_level = dp[0]
                if curr_level == next_level:
                    curr_node.next = next_node
                else:
                    curr_node.next = None
            
            if curr_node.left:
                dp.append((curr_node.left, curr_level + 1))
            if curr_node.right:
                dp.append((curr_node.right, curr_level + 1))
        
        #RETURN
        return dummy_node.left