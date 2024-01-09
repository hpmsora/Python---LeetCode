# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_list = []
        root2_list = []
        
        def helper(_root):
            if not (_root.left or _root.right):
                return [_root.val]
            sol = []
            if _root.left:
                sol += helper(_root.left)
            if _root.right:
                sol += helper(_root.right)
            
            return sol
        
        root1_list = helper(root1)
        root2_list = helper(root2)

        return root1_list == root2_list