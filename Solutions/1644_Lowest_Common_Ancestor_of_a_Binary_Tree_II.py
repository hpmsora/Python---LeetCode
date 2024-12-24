# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        sol = None
        # DFS
        def dfs(_root):
            nonlocal sol
            isPQ = False
            if _root == p or _root == q:
                isPQ = True

            left = False
            if _root.left and not sol:
                left = dfs(_root.left)
            
            right = False
            if _root.right and not sol:
                right = dfs(_root.right)

            if left and right or (isPQ and (left or right)) and not sol:
                sol = _root
                return True
            if left or right or isPQ:
                return True
            else:
                return False
        dfs(root)
        return sol