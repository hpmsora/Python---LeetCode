# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize data_list
        # [(node, depth level)...]
        dp = [(root, 0)]

        # Declare current level
        prev_depth = 0
        curr_sum = 0
        heap_sum = []
        heapq.heapify(heap_sum)
        # Loop - until dp empty (BFS)
        while dp:
            # Get first node
            curr_node, curr_depth = dp.pop(0)

            if prev_depth == curr_depth:
                curr_sum += curr_node.val
            else:
                heapq.heappush(heap_sum, (curr_sum, prev_depth))
                prev_depth = curr_depth
                curr_sum = curr_node.val

            # Check left side of current node
            if curr_node.left:
                # Add to dp if exist
                dp.append((curr_node.left, curr_depth+1))
            
            # Check right side of current node
            if curr_node.right:
                # Add to dp if exist
                dp.append((curr_node.right, curr_depth+1))
        heapq.heappush(heap_sum, (curr_sum, prev_depth))

        if len(heap_sum) < k:
            return -1
        else:
            res = heapq.nlargest(k, heap_sum)
            val, level = res[k - 1]
            #val, _ = heap_sum[prev_depth - k + 1]
            return val