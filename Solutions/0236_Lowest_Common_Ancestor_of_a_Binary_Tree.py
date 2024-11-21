# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(_root, _p, _q):
            if not _root:
                return None
            if _root == _p or _root == _q:
                return _root
            
            left = helper(_root.left, _p, _q)
            
            right = helper(_root.right, _p, _q)
            
            if left and right:
                return _root
            elif left:
                return left
            else:
                return right
        
        return helper(root, p, q)