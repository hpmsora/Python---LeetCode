# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        def helper(_root):
            if not _root:
                return True
            
            nonlocal prev
            val = _root.val
            left = True
            if _root.left:
                if val > _root.left.val:
                    left =  helper(_root.left)
                else:
                    return False
            if prev >= val:
                return False
            prev = val

            right = True
            if _root.right:
                if val < _root.right.val:
                    right =  helper(_root.right)
                else:
                    return False

            return left and right

        return helper(root)