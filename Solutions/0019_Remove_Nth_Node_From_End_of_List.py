# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(val=-1, next=head)
        order_dict = {}

        index = 1

        prev = head
        while head:
            order_dict[index] = head

            index += 1
            prev = head
            head = head.next
        index -= 1

        head = dummy.next
        if index-n == 0:
            return head.next
        head = order_dict[index - n]

        if head.next.next:
            head.next = head.next.next
        else:
            head.next = None

        return dummy.next