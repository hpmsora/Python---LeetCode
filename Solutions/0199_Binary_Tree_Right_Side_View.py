# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # BFS
        stack = collections.deque([(root, 0)])
        sol = []
        
        prev_depth = -1
        prev_val = None
        while stack:
            curr_node, curr_depth = stack.popleft()
            
            if not curr_depth == prev_depth:
                sol.append(prev_val)
                prev_depth = curr_depth
            prev_val = curr_node.val
            
            if curr_node.left:
                stack.append((curr_node.left, curr_depth + 1))
                
            if curr_node.right:
                stack.append((curr_node.right, curr_depth + 1))
            
        sol.append(curr_node.val)
        return sol[1:]