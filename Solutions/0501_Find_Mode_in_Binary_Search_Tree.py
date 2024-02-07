# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        num_dict = {}

        # BSF Searching
        def helper(_root:Optional[TreeNode]) -> None:
            # Update dictionary
            nonlocal num_dict
            val = _root.val
            if val in num_dict:
                num_dict[val] += 1
            else:
                num_dict[val] = 1
            
            # Leaf
            if not (_root.left or _root.right):
                return
            
            # Left
            if _root.left:
                helper(_root.left)

            # Right
            if _root.right:
                helper(_root.right)
            return

        # Run helper(BSF)
        helper(root)

        # Find max freq and keys
        sol = float('-inf')
        max_freq = 0
        for key, freq in num_dict.items():
            if freq > max_freq:
                sol = [key]
                max_freq = freq
            elif freq == max_freq:
                sol.append(key)
        
        # RETURN
        return sol