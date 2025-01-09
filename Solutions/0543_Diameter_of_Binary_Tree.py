# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sol = 0
        # dfs
        def dfs(_root):
            nonlocal sol
            if not (_root.left or _root.right):
                return 0
            left = 0
            if _root.left:
                left = dfs(_root.left) + 1

            right = 0
            if _root.right:
                right = dfs(_root.right) + 1

            sol = max(sol, left+right)

            return max(left, right)
        return max(dfs(root), sol)