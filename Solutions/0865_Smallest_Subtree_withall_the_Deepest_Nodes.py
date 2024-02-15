# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def helper(_root, _depth):
            if not(_root.left or _root.right):
                return (_root, _depth)
            
            left_node = None
            left_depth = -1
            if _root.left:
                left_node, left_depth = helper(_root.left, _depth + 1)
            
            right_node = None
            right_depth = -1
            if _root.right:
                right_node, right_depth = helper(_root.right, _depth + 1)

            if left_depth > right_depth:
                return (left_node, left_depth)
            elif left_depth < right_depth:
                return (right_node, right_depth)
            else:
                return (_root, left_depth)

        sol, _ = helper(root, 0)

        return sol
            