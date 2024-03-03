# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Save the head
        dummy = ListNode(val=-1, next=head)

        # Save the node to dictionary
        # key: index (int), val: node (ListNode)
        node_dict = {}

        # index save
        index = 0

        # Loop - all node
        while head:
            # Update node_dict
            node_dict[index] = head

            # Update head
            head = head.next

            # Update index
            index += 1

        # Find total length
        index = index - 1

        # Removing index
        removing_index = index - n

        # Removing condition
        if removing_index == -1: # removing first index
            dummy.next = dummy.next.next
        else: # removing not first index
            node_dict[removing_index].next = node_dict[removing_index].next.next

        # RETURN
        return dummy.next