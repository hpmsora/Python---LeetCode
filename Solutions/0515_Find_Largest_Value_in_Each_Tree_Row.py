# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        if not root:
            return sol

        stack = collections.deque([(root, 0)])
        max_num = float('-inf')
        prev_level = 0
        while stack:
            curr_node, level = stack.popleft()

            if level == prev_level:
                max_num = max(max_num, curr_node.val)
            else:
                sol.append(max_num)
                max_num = curr_node.val
                prev_level = level
            
            if curr_node.left:
                stack.append((curr_node.left, level+1))
            if curr_node.right:
                stack.append((curr_node.right, level+1))
        sol.append(max_num)
        return sol