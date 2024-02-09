"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        head_set = set()

        while p or q:
            if p:
                if p.val in head_set:
                    return p
                head_set.add(p.val)
                p = p.parent
            
            if q:
                if q.val in head_set:
                    return q
                head_set.add(q.val)
                q = q.parent