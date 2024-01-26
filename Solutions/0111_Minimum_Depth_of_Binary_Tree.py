# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(_root, _depth):
            if not (_root.left or _root.right):
                return _depth + 1
            
            sol = []
            if _root.left:
                sol.append(helper(_root.left, _depth + 1))

            if _root.right:
                sol.append(helper(_root.right, _depth + 1))
            
            return min(sol)
        
        if not root:
            return 0
        
        return helper(root, 0)