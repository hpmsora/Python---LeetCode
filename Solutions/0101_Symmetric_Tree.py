# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(_leftRoot, _rightRoot):
            if not(_leftRoot) and not(_rightRoot):
                return True
            if not(_leftRoot and _rightRoot):
                return False
            if _leftRoot.val != _rightRoot.val:
                return False
            leftBool = helper(_leftRoot.left, _rightRoot.right)
            if not leftBool:
                return False
            rightBool = helper(_rightRoot.left, _leftRoot.right)
            if not rightBool:
                return False
            return True

        if not(root.left or root.right):
            return True
        else:
            return helper(root.left, root.right)
