# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Special case
        if not root:
            return []
        # BFS
        dp = [(root, 0)]
        
        index = 0
        min_depth = 0
        max_depth = 0
        while index < len(dp):
            curr_node, depth = dp[index]
            # Left
            if curr_node.left:
                dp.append((curr_node.left, depth-1))
                min_depth = min(min_depth, depth-1)
            # Right
            if curr_node.right:
                dp.append((curr_node.right, depth+1))
                max_depth = max(max_depth, depth+1)
            index += 1
        sol = [[] for _ in range(min_depth, max_depth+1)]
        
        for each_dp, depth in dp:
            depth = depth - min_depth
            sol[depth].append(each_dp.val)
        return sol