"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # Boundary case - empty head
        if not head:
            new_node = Node(val=insertVal)
            new_node.next = new_node
            return new_node

        # reseve head
        dummy = Node(val=-1, next=head)

        # circular to list
        c_list = [dummy.next]
        
        # Loop - circular linked list 
        while True:
            # between nums
            if head.val <= insertVal and insertVal <= head.next.val:
                temp_head = head.next

                # insert num
                head.next = Node(val=insertVal, next=temp_head)
                break
            # first and last boundry
            if head.val > head.next.val:
                if head.val < insertVal or head.next.val > insertVal:
                    temp_head = head.next

                    # insert num
                    head.next = Node(val=insertVal, next=temp_head)
                    break

            # one loop done
            if head.next == dummy.next:
                temp_head = head.next

                # insert num
                head.next = Node(val=insertVal, next=temp_head)
                break

            # head and prev update
            head = head.next

        # RETURN
        return dummy.next