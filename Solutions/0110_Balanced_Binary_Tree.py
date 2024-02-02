# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # return: (depth: int, isValid: bool)
        def helper(_root, _depth):
            if not(_root.left or _root.right):
                return (_depth, True)
            
            left = _depth
            left_isValid = True
            if _root.left:
                left, left_isValid = helper(_root.left, _depth + 1)

            if not left_isValid:
                return (0, False)

            right = _depth
            right_isValid = True
            if _root.right:
                right, right_isValid = helper(_root.right, _depth + 1)

            if not right_isValid:
                return (0, False)
            
            if abs(left - right) <= 1:
                return (max(left, right), True)
            else:
                return (0, False)
        
        return helper(root, 0)[1]