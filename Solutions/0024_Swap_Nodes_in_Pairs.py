# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        last_head = dummy
        prev_head = None
        isSwap = False
        while head:
            if isSwap:
                last_head.next = head
                last_head = head.next
                head.next = prev_head
                prev_head.next = last_head
                last_head = prev_head
                head = prev_head.next
                isSwap = False
            else:
                prev_head = head
                head = head.next
                isSwap = True

        return dummy.next