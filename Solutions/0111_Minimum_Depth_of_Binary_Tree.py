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
        # helper - DFS
        def helper(_root):
            queue = collections.deque([(_root, 1)])
            while queue:
                node, depth = queue.popleft()
                if not (node.left or node.right):
                    return depth
                if node.left:
                    queue.append((node.left, depth+1))
                if node.right:
                    queue.append((node.right, depth+1))
        
        return helper(root)