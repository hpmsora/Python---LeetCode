# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Only one case
        if not head.next:
            # RETURN - original head
            return head
        
        # Slow, Fast varialbe
        slow = head.next
        fast = head.next.next

        # Loop - fast read the last second
        while fast and fast.next:
            # Update slow one step
            slow = slow.next

            # Update fast two step
            fast = fast.next.next
        
        # RETURN - slow (middle)
        return slow