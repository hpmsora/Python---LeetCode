# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) and (not list2):
            return list1
        last_sol = ListNode()
        sol = last_sol
        
        while list1 or list2:
            if not list1:
                last_sol.val = list2.val
                last_sol.next = list2.next
                break
            if not list2:
                last_sol.val = list1.val
                last_sol.next = list1.next
                break
            if list1.val < list2.val:
                last_sol.val = list1.val
                list1 = list1.next
            else:
                last_sol.val = list2.val
                list2 = list2.next
            last_sol.next = ListNode()
            last_sol = last_sol.next
        return sol