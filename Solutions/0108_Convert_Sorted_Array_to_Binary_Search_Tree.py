# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid_index = int(len(nums) / 2)
        num_tree = TreeNode(val=nums[mid_index])
        left_nums = nums[:mid_index]
        right_nums = nums[mid_index + 1:]
        if len(left_nums) > 0:
            num_tree.left = self.sortedArrayToBST(left_nums)
        if len(right_nums) > 0:
            num_tree.right = self.sortedArrayToBST(right_nums)
        return num_tree