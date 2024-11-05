# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        num_set = set()

        # DFS
        def helper(_root):
            if not _root:
                return False
            val = _root.val
            if k - val in num_set:
                return True
            else:
                num_set.add(val)
            
            # Left
            left = False
            if _root.left:
                left = helper(_root.left)
            if left:
                return True
            # Right
            right = False
            if _root.right:
                right = helper(_root.right)
            if right:
                return True
            
            return False

        return helper(root)