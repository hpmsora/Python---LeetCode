# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        max_list = {}
        max_depth = 0
        
        def helper(_root, _depth):
            val = _root.val
            nonlocal max_list, max_depth
            if _depth in max_list:
                max_list[_depth] = max(max_list[_depth], val)
            else:
                max_list[_depth] = val
            if not(_root.left or _root.right):
                max_depth = max(max_depth, _depth)
                return
            
            if _root.left:
                helper(_root.left, _depth + 1)
            
            if _root.right:
                helper(_root.right, _depth + 1)
                
            return
        
        helper(root, 0)
        sol = [0 for _ in range(max_depth + 1)]
        for key, val in max_list.items():
            sol[key] = val
            
        return sol