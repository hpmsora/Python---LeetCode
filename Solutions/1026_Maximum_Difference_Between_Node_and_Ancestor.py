# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def helper(_root, _max, _min):
            # Update max, min
            val = _root.val
            if _max < val:
                _max = val
            if _min > val:
                _min = val

            # Check leaf
            if not (_root.left or _root.right):
                return _max - _min

            # Left child
            left = 0
            if _root.left:
                left = max([_max - _min, helper(_root.left, _max, _min)])

            # Right child
            right = 0
            if _root.right:
                right = max([_max - _min, helper(_root.right, _max, _min)])
            
            # Return
            return max([left, right])

        return helper(root, float('-inf'), float('inf'))