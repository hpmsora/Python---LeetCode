# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(_root, _sum:int, _targetSum:int) -> bool:
            _sum = _sum + _root.val
            temp_sum = _sum
            if not (_root.left or _root.right):
                if _sum == _targetSum:
                    return True
                elif _sum > _targetSum:
                    return False
            sol = False
            if _root.left:
                sol = helper(_root.left, _sum, _targetSum)
            if sol:
                return True
            _sum = temp_sum
            if _root.right:
                sol = helper(_root.right, _sum, _targetSum)
            if sol:
                return True
            else:
                return False
        if not root:
            return False
        return helper(root, 0, targetSum)