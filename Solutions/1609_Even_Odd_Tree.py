# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([(root, 0)])

        if not root:
            return True
        
        n_val = root.val - 1
        n_depth = 0

        while queue:
            node, depth = queue.popleft()

            val = node.val

            if n_depth == depth:
                if n_depth % 2 == 0:
                    if val % 2 == 0:
                        return False
                    if n_val >= val:
                        return False
                    else:
                        n_val = val
                else:
                    if val % 2 == 1:
                        return False
                    if n_val <= val:
                        return False
                    else:
                        n_val = val
            else:
                n_depth = depth
                n_val = val
                if n_depth % 2 == 0:
                    if n_val % 2 == 0:
                        return False
                else:
                    if n_val % 2 == 1:
                        return False

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))
                
        return True