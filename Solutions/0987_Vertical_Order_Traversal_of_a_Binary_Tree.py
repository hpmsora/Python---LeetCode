# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [(root, 0, 0)]

        heap = []
        heapq.heapify(heap)

        left_min = 0
        right_max = 0

        while stack:
            curr_node, row, col = stack.pop()
            heapq.heappush(heap, (row, col, curr_node.val))

            if curr_node.left:
                stack.append((curr_node.left, row + 1, col - 1))
                left_min = min(col - 1, left_min)

            if curr_node.right:
                stack.append((curr_node.right, row + 1, col + 1))
                right_max = max(col + 1, right_max)
        
        sol = [[] for _ in range((right_max - left_min + 1))]

        while heap:
            _, col, val = heapq.heappop(heap)

            sol[col - left_min].append(val)

        return sol