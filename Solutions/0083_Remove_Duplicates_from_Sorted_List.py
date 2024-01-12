# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=float('-inf'), next=head)

        prev = dummy
        while head:
            if not head.val == prev.val:
                prev.next = head
                prev = head
            head = head.next
        prev.next = None
        
        return dummy.next_