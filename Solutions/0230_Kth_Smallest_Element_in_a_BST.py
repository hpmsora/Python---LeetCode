# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = collections.deque([root])

        q_list = []
        count = 0

        while queue:
            node = queue.popleft()
            if node:
                q_list.append(node.val)
                count += 1

                queue.append(node.left)
                queue.append(node.right)

        return sorted(q_list)[k - 1]