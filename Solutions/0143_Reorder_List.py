# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(val=-1, next=head)

        list_node = []

        while head:
            list_node.append(head)
            head = head.next

        new_list_node = []

        while list_node:
            f_node = list_node.pop(0)
            new_list_node.append(f_node)

            if list_node:
                new_list_node.append(list_node.pop())

        head = dummy
        for node in new_list_node:
            head.next = node
            head = head.next
        head.next = None