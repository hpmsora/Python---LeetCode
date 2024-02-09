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
        # Boundry case - empty root
        if not root:
            return root

        # Variables
        # linked list to list
        num_list = [] # [(val:int, node:Optional[Node])]

        # helper function - BSF
        # Return: None
        def helper(_root) -> None:
            val = _root.val

            # update num_list
            nonlocal num_list
            num_list.append((val, _root))

            # leaf check
            if not(_root.left or _root.right):
                return
            
            if _root.left: # left check
                helper(_root.left)
            
            if _root.right: # right check
                helper(_root.right)

            # RETURN
            return

        # Run helper function
        helper(root)

        # num_list sort
        num_list.sort()

        # First element
        _, first_num_node = num_list[0]
        
        # re-construct the link list
        dummy = Node(val=-1, left=first_num_node)

        # loop - left connection
        left_pointer = first_num_node
        for _, num_node in num_list[1:]:
            left_pointer.right = num_node
            left_pointer = left_pointer.right
        left_pointer.right = first_num_node

        # loop - left connection
        right_pointer = first_num_node
        for _, num_node in reversed(num_list[1:]):
            right_pointer.left = num_node
            right_pointer = right_pointer.left
        right_pointer.left = first_num_node

        # RETURN
        return dummy.left