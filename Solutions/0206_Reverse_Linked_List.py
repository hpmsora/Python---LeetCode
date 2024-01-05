# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        def helper(head):
            nonlocal stack
            if head:
                stack.append(head)
                head = head.next
                helper(head)
        
        helper(head)
        
        dummy = ListNode()
        prev = dummy
        for node in reversed(stack):
            prev.next = node
            prev = node
        prev.next = None
        
        return dummy.next