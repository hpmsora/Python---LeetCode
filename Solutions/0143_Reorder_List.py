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
        
        dummy_head = ListNode(val=0, next=head)
        head_dict = {}
        max_index = 0
        while head:
            head_dict[max_index] = head
            head = head.next
            max_index += 1
        max_index -= 1
        head = dummy_head
        for each_index in range(max_index//2+1):
            head.next = head_dict[each_index]
            head = head.next
            
            head.next = head_dict[max_index - each_index]
            head = head.next
        if max_index % 2 == 1:
            head.next = None
        else:
            head.next = head_dict[max_index//2]
            head.next.next = None