# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.num_list = []
        self.index = 0
        
        def dfs(_root):
            if _root.left:
                dfs(_root.left)
            self.num_list.append(_root.val)
            if _root.right:
                dfs(_root.right)
        dfs(root)

    def next(self) -> int:
        self.index += 1
        return self.num_list[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < len(self.num_list)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()