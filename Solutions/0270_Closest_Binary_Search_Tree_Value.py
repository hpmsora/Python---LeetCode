# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff = float("inf")
        sol = []
        def helper(_root):
            val = _root.val
            nonlocal diff, sol, target
            if abs(target - val) < diff:
                diff = abs(target - val)
                sol = [val]
            elif abs(target - val) == diff:
                sol.append(val)
                
            if not(_root.left or _root.right):
                return
            
            if _root.left:
                helper(_root.left)
            
            if _root.right:
                helper(_root.right)
                
            return
        
        helper(root)
        
        return min(sol)