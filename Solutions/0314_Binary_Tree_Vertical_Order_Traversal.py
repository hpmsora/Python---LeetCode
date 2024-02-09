# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Boundry case - empty root
        if not root:
            return []

        # Global min pos and max pos
        min_pos = 0
        max_pos = 0

        # DFS
        def helper(_root):
            # Global variables
            nonlocal min_pos, max_pos

            # Init queue
            # (node, v_pos)
            queue = collections.deque([(_root, 0)])
            # [(val:int, v_pos:int)]
            node_list = []

            # Loop - Queue
            while queue:
                node, pos = queue.popleft() # Get left most queue

                # node_list Update
                node_list.append((node.val, pos))

                # Global min, max pos updaet
                min_pos = min(min_pos, pos)
                max_pos = max(max_pos, pos)

                if node.left: # Left check
                    queue.append((node.left, pos - 1))
                if node.right: # Right check
                    queue.append((node.right, pos + 1))
            
            #RETURN
            return node_list

        # Run helper
        node_list = helper(root)

        # Re-arrange node_list
        sol = [[] for _ in range(max_pos - min_pos + 1)]
        for val, pos in node_list:
            sol[pos - min_pos].append(val)

        # RETURN
        return sol