# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # BFS
        stack = collections.deque([(root, 0)])
        min_depth = 0
        max_depth = 0
        index = 0
        
        while index < len(stack):
            curr_node, depth = stack[index]
            
            min_depth = min(min_depth, depth)
            max_depth = max(max_depth, depth)
            
            if curr_node.left:
                stack.append((curr_node.left, depth - 1))
            
            if curr_node.right:
                stack.append((curr_node.right, depth + 1))
            
            index += 1
        
        total_depth = max_depth - min_depth
        
        sol = [[] for _ in range(min_depth, max_depth+1)]
        
        
        for node, depth in stack:
            sol[depth - min_depth].append(node.val)
        return sol