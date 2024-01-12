-# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(val=-1)
        head_pointer = dummy

        sol_list = []

        while head:
            sol_list.append((head.val, head))
            head = head.next

        sol_list.sort(key=lambda x: x[0])
        
        for _, sol in sol_list:
            head_pointer.next = sol
            head_pointer = head_pointer.next
        head_pointer.next = None

        return dummy.next