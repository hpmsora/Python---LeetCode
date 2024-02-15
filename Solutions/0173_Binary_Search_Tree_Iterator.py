# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root_list = []

        # helper - BSF
        def helper(_root):
            if not(_root.left or _root.right):
                return [_root.val]
            
            left = []
            if _root.left:
                left = helper(_root.left)
            
            right = []
            if _root.right:
                right = helper(_root.right)
            
            return left + [_root.val] + right
        
        if root:
            self.root_list = helper(root)

    def next(self) -> int:
        if self.root_list:
            return self.root_list.pop(0)

    def hasNext(self) -> bool:
        if self.root_list:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()