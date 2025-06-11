"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        queue = head
        if not head:
            return

        while queue:
            old_to_new[queue] = Node(x=queue.val)
            queue = queue.next
        
        sol = old_to_new[head]
        queue = head
        while queue:
            new_node = old_to_new[queue]
            if queue.random:
                new_node.random = old_to_new[queue.random]
            
            if queue.next:
                new_node.next = old_to_new[queue.next]
            queue = queue.next
        return sol