# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        # DFS
        def dfs(_root):
            num = str(_root.val)

            # Left
            left = []
            if _root.left:
                left = [num + value for value in dfs(_root.left)]

            # Right
            right = []
            if _root.right:
                right = [num + value for value in dfs(_root.right)]
            
            if left or right:
               return left + right
            else:
                return [num]
        sol = 0
        for each_num in dfs(root):
            sol += int(each_num)
        return sol