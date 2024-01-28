# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subRoot_start = subRoot.val
        def helper(_root):
            val = _root.val
            
            nonlocal subRoot_start
            isValid = False
            if val == subRoot_start:
                isValid = isSame(_root, subRoot)
            
            if isValid:
                return True
            
            if not(_root.left or _root.right):
                return False
            
            if _root.left:
                isValid = helper(_root.left)
                if isValid:
                    return True
            if _root.right:
                isValid = helper(_root.right)
                if isValid:
                    return True
            
            return isValid
        
        def isSame(_root_1, _root_2):
            val_1 = _root_1.val
            val_2 = _root_2.val
            
            if not val_1 == val_2:
                return False
            
            left = False
            if _root_1.left:
                if _root_2.left:
                    left = isSame(_root_1.left,_root_2.left)
                else:
                    return False
            else:
                if _root_2.left:
                    return False
                else:
                    left = True
            
            if not left:
                return False
            
            right = False
            if _root_1.right:
                if _root_2.right:
                    right = isSame(_root_1.right,_root_2.right)
                else:
                    return False
            else:
                if _root_2.right:
                    return False
                else:
                    right = True
            
            if not right:
                return False

            return True
        return helper(root)