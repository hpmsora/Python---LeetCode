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
        stack = [(root, 0)]

        index = 0
        min_order = 0
        max_order = 0

        while index < len(stack):
            curr_node, order = stack[index]
            min_order = min(min_order, order)
            max_order = max(max_order, order)

            if curr_node.left:
                stack.append((curr_node.left, order-1))
            
            if curr_node.right:
                stack.append((curr_node.right, order + 1))
            index += 1
        
        sol = [[] for _ in range((max_order - min_order+1))]

        for node, order in stack:
            order = order - min_order
            sol[order].append(node.val)
        
        return sol