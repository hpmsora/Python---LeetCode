# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = len(postorder) - 1
        mp = {val: i for i, val in enumerate(inorder)}
        
        def build(s, e):
            nonlocal idx
            if s > e:
                return None
            root_val = postorder[idx]
            idx -= 1
            root = TreeNode(root_val)
            id = mp[root_val]
            root.right = build(id + 1, e)
            root.left = build(s, id - 1)
            return root
        
        return build(0, len(inorder) - 1)