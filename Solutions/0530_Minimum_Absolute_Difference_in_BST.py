# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sol = float('inf')
        pre = None
        def helper(_root):
            nonlocal sol, pre
            if not _root:
                return

            helper(_root.left)
            if not pre == None:
                sol = min(sol, _root.val - pre)

            pre = _root.val

            helper(_root.right)
            
        helper(root)
        return sol