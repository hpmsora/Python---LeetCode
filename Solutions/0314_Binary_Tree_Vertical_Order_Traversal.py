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
        left = 0
        right = 0
        data_dict = {}
        
        queue = collections.deque([(root, 0)])
        
        while queue:
            curr_node, level = queue.popleft()
            left = min(left, level)
            right = max(right, level)
            
            if level in data_dict:
                data_dict[level].append(curr_node.val)
            else:
                data_dict[level] = [curr_node.val]
            
            if curr_node.left:
                queue.append((curr_node.left, level-1))
            
            if curr_node.right:
                queue.append((curr_node.right, level+1))
                
        sol = [[] for _ in range(right - left + 1)]
        
        for index, data in data_dict.items():
            sol[index-left] = data
        return sol