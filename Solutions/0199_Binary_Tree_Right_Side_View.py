# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Speical Case - Empty
        if not root:
            return []
        
        # BFS
        dp = [(root, 0)]
        
        prev_depth = -1
        prev_num = None
        sol = []
        while dp:
            curr_node, depth = dp.pop(0)
            
            if not prev_depth == depth:
                sol.append(prev_num)
                prev_depth = depth
            
            # left
            if curr_node.left:
                dp.append((curr_node.left, depth + 1))
            
            # right
            if curr_node.right:
                dp.append((curr_node.right, depth + 1))
                
            prev_num = curr_node.val
        sol.append(prev_num)
        return sol[1:]