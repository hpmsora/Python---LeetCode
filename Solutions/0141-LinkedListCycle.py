# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_set = set()

        # First
        isFirst = True
        while head:
            if isFirst:
                visited_set.add(head)
                isFirst = False
            else:
                if head in visited_set:
                    return True
                else:
                    visited_set.add(head)
            head = head.next
        return False