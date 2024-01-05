# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total_max = -1 * float('inf')
        def helper(root):
            val = root.val
            left = -1 * float('inf')
            if root.left:
                left = helper(root.left)
            right = -1 * float('inf')
            if root.right:
                right = helper(root.right)
            if not (root.left or root.right):
                return val
            
            local_max = max(left + val, right + val, val)
            nonlocal total_max
            total_max = max(total_max, local_max, right, left, right+left+val)
            return local_max
        return max(helper(root), total_max)