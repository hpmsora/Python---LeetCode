# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        sol = []

        stack = collections.deque([(root, 0)])

        while stack:
            curr_node, depth = stack.popleft()

            if len(sol) - 1 < depth:
                sol.append([curr_node.val])
            else:
                if depth % 2 == 0:
                    sol[depth].append(curr_node.val)
                else:
                    sol[depth] = [curr_node.val] + sol[depth]
            if curr_node.left:
                stack.append((curr_node.left, depth + 1))
            if curr_node.right:
                stack.append((curr_node.right, depth + 1))
        return sol