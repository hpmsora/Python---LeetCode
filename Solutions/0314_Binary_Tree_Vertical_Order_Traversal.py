# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Special case - empty root
        if not root:
            return []
        
        # min, max column number declare
        min_col = 0
        max_col = 0
        
        # column dictinary
        # key: int(col)
        # value: list(int(val))
        col_dict = {}

        # BFS
        # dp = [(TreeNode, int(col)),...]
        dp = [(root, 0)]
        while dp:
            # Get first node info
            curr_node, col = dp.pop(0)

            # column dictionary update
            if col in col_dict:
                col_dict[col].append(curr_node.val)
            else:
                col_dict[col] = [curr_node.val]

            # min, max col update
            if min_col > col:
                min_col = col
            elif max_col < col:
                max_col = col

            # Left
            if curr_node.left:
                dp.append((curr_node.left, col - 1))
            
            # Right
            if curr_node.right:
                dp.append((curr_node.right, col + 1))

        # solution variable
        sol = []

        # Loop - column number from min col to max col
        for col_num in range(min_col, max_col + 1):
            # Add to sol list the value list
            sol.append(col_dict[col_num])
        
        # RETURN - sol
        return sol