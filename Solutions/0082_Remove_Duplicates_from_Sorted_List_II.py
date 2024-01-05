# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-101)
        prev = dummy
        while head:
            val = head.val
            count = 1
            while head.next:
                if head.next.val == val:
                    count += 1
                    head = head.next
                else:
                    break
            if count == 1:
                prev.next = head
                prev = prev.next
            head = head.next
        prev.next = None
        return dummy.next