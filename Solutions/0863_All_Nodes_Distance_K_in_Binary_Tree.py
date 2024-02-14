# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Return varialbe
        sol = []

        # Helper function - BFS (find val under _root with k distance)
        def helper(_root, _k):
            if _k == 0:
                return [_root.val]

            # Leaf check
            if not (_root.left or _root.right):
                return []
            
            # Left check
            left = []
            if _root.left:
                left = helper(_root.left, _k - 1)

            # Right check
            right = []
            if _root.right:
                right = helper(_root.right, _k - 1)

            # RETURN
            return left + right

        # Helper function - BFS (find ancestor)
        def helper_2(_root):
            nonlocal target
            if target == _root:
                return [_root]

            # Leaf check
            if not (_root.left or _root.right):
                return []
            
            # Left check
            if _root.left:
                left = helper_2(_root.left)
                if left:
                    return left + [_root]

            # Right check
            if _root.right:
                right = helper_2(_root.right)
                if right:
                    return right + [_root]


            # RETURN
            return []

        # Helper function - BFS (find val under _root with k distance except visited)
        def helper_3(_root, _k, _exception):
            # Exception break
            if _root == _exception:
                return []

            if _k == 0:
                return [_root.val]

            # Leaf check
            if not (_root.left or _root.right):
                return []
            
            # Left check
            left = []
            if _root.left:
                left = helper_3(_root.left, _k - 1, _exception)

            # Right check
            right = []
            if _root.right:
                right = helper_3(_root.right, _k - 1, _exception)

            # RETURN
            return left + right

        # 1. Check child of target
        sol = sol + helper(target, k)

        # 2. Find ancesstor of target
        ancestor = helper_2(root)
        
        # 3. Find ancestor's target distance
        # Loop all acestor iteration except target
        prev = ancestor[0] # BFS exception (previous ancestor)
        for index, each_ancestor in enumerate(ancestor[1:]):
            sol = sol + helper_3(each_ancestor, k - index - 1, prev)

            # Update previous ancestor
            prev = each_ancestor
        
        # RETURN
        return sol