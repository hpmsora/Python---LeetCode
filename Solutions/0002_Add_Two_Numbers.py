# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        added = ListNode()
        link_added = added
        carry = int
        carry = 0
        l1_next = None
        l2_next = None
        while l1 or l2:
            l1_val = 0
            l2_val = 0
            if not l1:
                l1_val = 0
            else:
                l1_val = l1.val
                l1_next = l1.next
            if not l2:
                l2_val = 0
            else:
                l2_val = l2.val
                l2_next = l2.next

            sum_l1_l2 = l1_val + l2_val + carry
            carry = int(sum_l1_l2 / 10)
            sum_l1_l2 = sum_l1_l2 % 10
            link_added.val = sum_l1_l2
            if l1_next or l2_next:
                link_added.next = ListNode()
                link_added = link_added.next

            l1 = l1_next
            l2 = l2_next
        if carry == 0:
            link_added = None
        else:
            link_added.next = ListNode()
            link_added = link_added.next
            link_added.val = carry
        return added