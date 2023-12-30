# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(_preorder, _inorder):
            if not _preorder:
                return None
            if not _inorder:
                return None
            
            n = _preorder.pop(0)
            root = TreeNode(val=n)
            left_inorder = []
            right_inorder = []

            for index in range(len(_inorder)):
                if n == _inorder[index]:
                    left_inorder = _inorder[:index]
                    right_inorder = _inorder[index+1:]
                    break

            root.left = helper(_preorder, left_inorder)
            root.right = helper(_preorder, right_inorder)
            return root
        
        return helper(preorder, inorder)