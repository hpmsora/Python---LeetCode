# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # BFS
        stack = collections.deque([(root, 1)])
        while stack:
            curr_node, depth = stack.popleft()
            
            if (not curr_node.left) and (not curr_node.right):
                return depth
            
            if curr_node.left:
                stack.append((curr_node.left, depth + 1))
            if curr_node.right:
                stack.append((curr_node.right, depth + 1))