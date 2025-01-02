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
        p_set = set([p])
        q_set = set([q])

        while p or q:
            if p in q_set:
                return p
            else:
                p_set.add(p)
            if q in p_set:
                return q
            else:
                q_set.add(q)
            if p:
                p = p.parent
            if q:
                q = q.parent