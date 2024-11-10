# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        dp = [root]
        
        # BFS
        while dp:
            curr_node = dp.pop(0)
            
            if curr_node == None:
                for each_dp in dp:
                    if not each_dp == None:
                        return False
                return True
            
            if curr_node.left:
                dp.append(curr_node.left)
            else:
                dp.append(None)
            
            if curr_node.right:
                dp.append(curr_node.right)
            else:
                dp.append(None)