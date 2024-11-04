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
            # p, q set update
            p_set.add(p)
            q_set.add(q)

            # p check:
            if p in q_set:
                return p
            # q check:
            if q in p_set:
                return q

            # p update
            if p:
                p = p.parent
            # q update
            if q:
                q = q.parent