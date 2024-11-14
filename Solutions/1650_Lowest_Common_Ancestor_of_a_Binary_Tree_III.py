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
        p_set = set()
        q_set = set()
        while p or q:
            p_set.add(p)
            q_set.add(q)
            if q in p_set:
                return q
            elif p in q_set:
                return p
            if p.parent:
                p = p.parent
            if q.parent:
                q = q.parent
        return None