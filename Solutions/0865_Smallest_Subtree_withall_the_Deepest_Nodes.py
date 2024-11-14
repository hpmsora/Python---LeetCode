# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        # dp List = [(node, parent's list, depth)...]
        dp = [(root, [], 0)]
        node_dict = {}
        
        same_depth = []
        prev_depth = -1
        while dp:
            dp_element = dp.pop(0)
            curr_node, parent_node_list, depth = dp_element
            node_dict[curr_node.val] = curr_node
            
            if not depth == prev_depth:
                same_depth = [dp_element]
                prev_depth = depth
            else:
                same_depth.append(dp_element)
            
            # Left
            if curr_node.left:
                dp.append((curr_node.left, [curr_node.val] + parent_node_list, depth + 1))
            # Right
            if curr_node.right:
                dp.append((curr_node.right, [curr_node.val] + parent_node_list, depth + 1))
        parent_list_set = []
        heap = []
        heapq.heapify(heap)
        
        for each_curr_node, each_parent_list, _ in same_depth:
            parent_list = [each_curr_node.val] + each_parent_list
            parent_list_set.append(set(parent_list))
            heapq.heappush(heap, (len(parent_list), parent_list))
            
        _, shortest = heapq.heappop(heap)
        for each_shortest in shortest:
            isSol = True
            for each_parent_list_set in parent_list_set:
                if not each_shortest in each_parent_list_set:
                    isSol = False
                    break
            if isSol:
                return node_dict[each_shortest]
        return []