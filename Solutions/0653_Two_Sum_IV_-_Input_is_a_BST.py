# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = collections.deque([root])
        num_set = set()
        
        while queue:
            curr_node = queue.popleft()
            
            curr_val = curr_node.val
            if k - curr_val in num_set:
                return True
            
            num_set.add(curr_val)
            
            if curr_node.left:
                queue.append(curr_node.left)
            
            if curr_node.right:
                queue.append(curr_node.right)
        return False