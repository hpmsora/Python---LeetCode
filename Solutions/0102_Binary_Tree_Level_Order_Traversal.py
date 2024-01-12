# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol_dict = {}

        if not root:
            return []

        def helper(_root, _depth):
            nonlocal sol_dict
            if _depth in sol_dict:
                sol_dict[_depth].append(_root.val)
            else:
                sol_dict[_depth] = [_root.val]
            
            if not(_root.left or _root.right):
                return _depth
            
            left = 0
            if _root.left:
                left = helper(_root.left, _depth+1)
            
            right = 0
            if _root.right:
                right = helper(_root.right, _depth+1)
            
            return max([left, right])
        
        max_depth = helper(root, 1)

        sol = [[] for _ in range(max_depth)]

        for key, val in sol_dict.items():
            sol[key-1] = val
        
        return sol