# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(_root, _prev):
            sol = 0
            val = _prev*10+_root.val
            if _root.left:
                sol += helper(_root.left, val)
            if _root.right:
                sol += helper(_root.right, val)

            if not (_root.right or _root.left):
                sol = val
            return sol
        return helper(root, 0)