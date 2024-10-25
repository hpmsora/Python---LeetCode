# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # DFS - Double root
        def helper(_root1, _root2):
            if _root1:
                if _root2:
                    if not _root1.val == _root2.val:
                        return False
                else:
                    return False
            elif _root2:
                return False
            else:
                return True
            
            # root1 children
            root1_child = [] # [(val, node)...]

            # root2 children
            root2_child = [] # [(val, node)...]

            # Left root1
            if _root1.left:
                root1_child.append((_root1.left.val, _root1.left))
            
            # Right root1
            if _root1.right:
                root1_child.append((_root1.right.val, _root1.right))
            
            # Left root2
            if _root2.left:
                root2_child.append((_root2.left.val, _root2.left))
            
            # Right root2
            if _root2.right:
                root2_child.append((_root2.right.val, _root2.right))

            # Check 1: Size test
            if not len(root1_child) == len(root2_child):
                return False

            # Check 2: value test
            set_list = [] # [(node, node)...]
            for each_root1_child_val, each_root1_child_node in root1_child:
                index = 0
                while index < len(root2_child):
                    each_root2_child_val, each_root2_child_node = root2_child[index]
                    if each_root1_child_val == each_root2_child_val:
                        set_list.append((each_root1_child_node, each_root2_child_node))
                        break
                    index += 1
                if index == len(root2_child):
                    return False
            
            # Check 3: node test
            for each_root1_child_node, each_root2_child_node in set_list:
                if not helper(each_root1_child_node, each_root2_child_node):
                    return False
            
            # Pass all test
            return True
            
        # RETURN
        return helper(root1, root2)

