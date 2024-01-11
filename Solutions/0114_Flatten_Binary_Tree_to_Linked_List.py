# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(_root):
            if not(_root.left or _root.right):
                return [_root]
            
            sol = [_root]
            if _root.left:
                sol += helper(_root.left)
            if _root.right:
                sol += helper(_root.right)
            
            return sol

        if root:
            sol_list = helper(root)
            dummy = TreeNode(val=-1)
            head = dummy
            for sol in sol_list:
                head.right = sol
                head.left = None
                head =head.right
            head.next = None
            root = dummy.right