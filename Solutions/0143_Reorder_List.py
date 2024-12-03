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
        start = ListNode(next=head)
        
        node_list = []
        
        while head:
            node_list.append(head)
            head = head.next
        
        left = 0
        right = len(node_list) - 1
        prev_node = start
        isTrue = False
        while left < right:
            left_node = node_list[left]
            right_node = node_list[right]
            prev_node.next = left_node
            left_node.next = right_node
            prev_node = right_node
            left += 1
            right -= 1
            
        if len(node_list) % 2 == 1:
            prev_node.next = node_list[len(node_list) // 2]
            prev_node.next.next = None
        else:
            prev_node.next = None