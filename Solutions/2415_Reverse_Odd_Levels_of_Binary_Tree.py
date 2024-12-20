# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS
        stack = collections.deque([(root, 0)])

        prev_level = -1
        reverse_stack = []
        while stack:
            curr_node, level = stack.popleft()
            if curr_node.left:
                stack.append((curr_node.left, level + 1))
                stack.append((curr_node.right, level + 1))
            if level == prev_level:
                if level % 2 == 1:
                    reverse_stack.append(curr_node)
                else:
                    pass
            else:
                if level % 2 == 1:
                    reverse_stack.append(curr_node)
                else:
                    left = 0
                    right = len(reverse_stack) - 1
                    while left < right:
                        reverse_stack[left].val, reverse_stack[right].val = reverse_stack[right].val, reverse_stack[left].val
                        left += 1
                        right -= 1
                    reverse_stack = []
                prev_level = level
        if prev_level % 2 == 1:
            left = 0
            right = len(reverse_stack) - 1
            while left < right:
                reverse_stack[left].val, reverse_stack[right].val = reverse_stack[right].val, reverse_stack[left].val
                left += 1
                right -= 1
        return root