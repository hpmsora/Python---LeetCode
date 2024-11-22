# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(_root, _total):
            if not (_root.left or _root.right):
                return _total * 10 + _root.val
            
            sol = 0
            if _root.left:
                sol += helper(_root.left, _total * 10 + _root.val)
            
            if _root.right:
                sol += helper(_root.right, _total * 10 + _root.val)
            return sol
        
        return helper(root, 0)