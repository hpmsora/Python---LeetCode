# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        if not (head.next):
            return head
        else:
            head_pointer = head.next

        head_size = 1
        dummy = ListNode(val=0, next=head)
        last_pointer = dummy.next

        while last_pointer.next:
            head_size += 1
            last_pointer = last_pointer.next
        
        k = k % head_size

        if k == 0:
            return head

        k = head_size - k
        head_pointer = dummy.next
        cut_pointer = head_pointer

        while not k == 0:
            k -= 1
            if k == 0:
                head_pointer = cut_pointer.next
                cut_pointer.next = None
                break
            cut_pointer = cut_pointer.next

        last_pointer.next = dummy.next

        return head_pointer