# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # helper - BFS
        # Return: ['TreeNode']
        def helper(_root, _target):
            # return value
            sol = []

            # val check
            val = _root.val
            if val == _target.val:
                sol.append(_root)
                return sol

            # Leaf check
            if not(_root.left or _root.right):
                return sol
            
            # Left check
            left = []
            if _root.left:
                left = helper(_root.left, _target)
            
            # Left solution exist
            if left:
                left.append(_root)
                return left

            # Right check
            right = []
            if _root.right:
                right = helper(_root.right, _target)

            # Right solution exist
            if right:
                right.append(_root)
                return right
            
            # RETURN
            return sol

        # Run helper
        p_list = helper(root, p)
        q_list = helper(root, q)

        # Loop - find common element
        for each_p in p_list:
            for each_q in q_list:
                if each_p == each_q:
                    return each_p