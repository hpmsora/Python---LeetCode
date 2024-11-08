# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # DFS
        # RETURN: Parents List
        def helper(_root, _target) -> 'TreeNode':
            if _root == _target:
                return [_root]
            
            # Left
            left = []
            if _root.left:
                left = helper(_root.left, _target)
                if left:
                    return left + [_root]
            # Right
            right = []
            if _root.right:
                right = helper(_root.right, _target)
                if right:
                    return right + [_root]

        p_list = helper(root, p)
        q_list = set(helper(root, q))

        for each_p_list in p_list:
            if each_p_list in q_list:
                return each_p_list