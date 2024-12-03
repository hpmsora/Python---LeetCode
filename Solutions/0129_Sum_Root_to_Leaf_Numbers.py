# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # DFS
        def dfs(_root, _num):
            
            if not (_root.left or _root.right):
                return _num * 10 + _root.val

            left = 0
            if _root.left:
                left = dfs(_root.left, _num * 10 + _root.val)

            right = 0
            if _root.right:
                right = dfs(_root.right, _num * 10 + _root.val)
            
            return left + right

        return dfs(root, 0)