# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        def helper(_root):
            nonlocal max_length

            if not (_root.left or _root.right):
                return 0

            left = 0
            if _root.left:
                left = helper(_root.left) + 1
            
            right = 0
            if _root.right:
                right = helper(_root.right) + 1
            
            max_length = max(max_length, left+right)

            return max(left, right)
        
        return max(helper(root), max_length)