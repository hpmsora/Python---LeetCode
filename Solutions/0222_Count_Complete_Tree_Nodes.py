# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root.left and root.right:
                return 1 + helper(root.left) + helper(root.right)
            elif root.left:
                return 2
            else:
                return 1
        if not root:
            return 0
        return helper(root)