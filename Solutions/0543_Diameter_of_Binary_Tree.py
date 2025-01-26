# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sol = 0
        def dfs(_root):
            nonlocal sol

            if not (_root.left or _root.right):
                return 1
            left = 0
            if _root.left:
                left = dfs(_root.left)
            right = 0
            if _root.right:
                right = dfs(_root.right)
            
            sol = max(sol, left + right)

            return max(left, right) + 1
        
        dfs(root)

        return sol