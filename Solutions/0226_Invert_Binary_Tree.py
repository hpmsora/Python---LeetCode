# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            temp_root = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp_root)
            return root
        else:
            return root