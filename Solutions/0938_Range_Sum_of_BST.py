# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(_root, _low, _high):
            if not _root:
                return 0
            val = _root.val

            if not (_root.left or _root.right):
                if _low <= val and val <= _high:
                    return val
                else:
                    return 0

            if val < _low:
                return helper(_root.right, _low, _high)
            elif val > _high:
                return helper(_root.left, _low, _high)
            else:
                return val + helper(_root.left, _low, _high) + helper(_root.right, _low, _high)
        return helper(root, low, high)