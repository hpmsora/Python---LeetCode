# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def helper(_root):
            val = _root.val
            if not(_root.left or _root.right):
                return [val]
            
            left = []
            if _root.left:
                left = helper(_root.left)
            
            right = []
            if _root.right:
                right = helper(_root.right)

            return [val] + left + right

        return helper(root)