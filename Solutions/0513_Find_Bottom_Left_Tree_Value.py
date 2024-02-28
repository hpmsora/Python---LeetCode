# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def helper(_root):
            queue = collections.deque([(_root, 0)])

            most_left = _root
            most_depth = 0

            while queue:
                node, depth = queue.popleft()
                if node.left:
                    queue.append((node.left, depth+1))
                if node.right:
                    queue.append((node.right, depth+1))

                if most_depth < depth:
                    most_left = node
                    most_depth = depth
                    print(most_depth)
            return most_left.val
        return helper(root)