# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        f_head = ListNode(val = -101)
        b_head = ListNode(val = -101)

        f_pointer = f_head
        b_pointer = b_head

        while head:
            if not head:
                break
            val = head.val

            if val >= x:
                b_pointer.next = head
                b_pointer = b_pointer.next
            else:
                f_pointer.next = head
                f_pointer = f_pointer.next
            
            head = head.next

        sol = None
        if f_head.next:
            sol = f_head.next
        else:
            return b_head.next
        if b_head.next:
            f_pointer.next = b_head.next
            b_pointer.next = None
        return sol