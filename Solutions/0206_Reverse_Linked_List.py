# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        link_list = []

        while head:
            link_list.append(head)
            head = head.next

        index = 1
        dummy = ListNode(val=-1, next=None)
        new_head = dummy
        while index <= len(link_list):
            node = link_list[len(link_list) - index]
            new_head.next = node
            new_head = new_head.next
            index += 1
        
        new_head.next = None

        return dummy.next