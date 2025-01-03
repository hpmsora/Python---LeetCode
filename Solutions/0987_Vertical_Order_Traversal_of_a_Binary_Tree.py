# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        heap = []

        stack = collections.deque([(root, 0, 0)]) # (node, col, row, val)

        col_min = 0
        col_max = 0

        while stack:
            curr_node, col, row = stack.popleft()

            heap.append((col, row, curr_node.val))

            if curr_node.left:
                stack.append((curr_node.left, col-1, row+1))
                col_min = min(col_min, col-1)
            if curr_node.right:
                stack.append((curr_node.right, col+1, row+1))
                col_max = max(col_max, col+1)
        
        heapq.heapify(heap)

        sol = [[] for _ in range(col_max - col_min + 1)]

        while heap:
            col, _, val = heapq.heappop(heap)
            sol[col - col_min].append(val)
        return sol