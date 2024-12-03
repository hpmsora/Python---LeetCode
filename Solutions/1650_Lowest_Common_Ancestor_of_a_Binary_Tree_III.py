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
        p_set.add(p.val)
        q_set.add(q.val)
        
        while p or q:
            if p:
                if p.val in q_set:
                    return p
                else:
                    p = p.parent
                    if p:
                        p_set.add(p.val)
            if q:
                if q.val in p_set:
                    return q
                else:
                    q = q.parent
                    if q:
                        q_set.add(q.val)