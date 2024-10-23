# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # [(node, parent node, level, direct child sum)...]
        queue = collections.deque([(root, 0, 0)])

        sum_level = 0
        prev_level = 0
        while queue:
            curr_node, level, child_sum = queue.popleft()
            
            if not prev_level == level:
                sum_level = curr_node.val
                for each_queue in queue:
                    each_curr_node, _, _ = each_queue
                    sum_level += each_curr_node.val

            curr_node.val = sum_level - child_sum

            child_sum = 0
            if curr_node.left:
                child_sum += curr_node.left.val
            if curr_node.right:
                child_sum += curr_node.right.val

            if curr_node.left:
                queue.append((curr_node.left, level+1, child_sum))
            
            if curr_node.right:
                queue.append((curr_node.right, level+1, child_sum))
            
            prev_level = level

        return root