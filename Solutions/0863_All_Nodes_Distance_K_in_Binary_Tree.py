# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_node_list = []

        def dfs(_root, _parent_list):
            nonlocal parent_node_list
            if _root == target:
                parent_node_list = _parent_list
                return
            if _root.left:
                dfs(_root.left, [_root] + _parent_list)
            
            if _root.right:
                dfs(_root.right, [_root] + _parent_list)
        dfs(root, [])

        sol = []

        # 1. below currnet target
        def dfs_k(_root, _steps, _exception):
            nonlocal sol
            if _steps == 0:
                sol.append(_root.val)
                return
            if _root.left and not _root.left == _exception:
                dfs_k(_root.left, _steps - 1, _exception)
            if _root.right and not _root.right == _exception:
                dfs_k(_root.right, _steps - 1, _exception)
        
        dfs_k(target, k, None)

        # 2. Above target
        prev_node = target
        k_steps = k - 1
        for each_parent in parent_node_list:
            dfs_k(each_parent, k_steps, prev_node)
            prev_node = each_parent
            k_steps -= 1
            if k_steps < 0:
                break
        return sol