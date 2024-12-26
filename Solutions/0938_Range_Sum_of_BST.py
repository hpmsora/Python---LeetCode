# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # DFS
        def dfs(_root):

            if _root.val < low:
                # Right
                if _root.right:
                    return dfs(_root.right)
                else:
                    return 0
            elif _root.val > high:
                # Left
                if _root.left:
                    return dfs(_root.left)
                else:
                    return 0
            else:
                # Left
                left = 0
                if _root.left:
                    left = dfs(_root.left)
                
                # Right
                right = 0
                if _root.right:
                    right = dfs(_root.right)
                return left + right + _root.val
        return dfs(root)