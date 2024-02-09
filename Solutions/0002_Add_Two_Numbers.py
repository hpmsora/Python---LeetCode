# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reserve original link list
        dummy_1 = ListNode(val=-1, next=l1)
        dummy_2 = ListNode(val=-1, next=l2)
        
        # variables
        carry = 0
        longer_l = dummy_2 # solution (l2 prior)
        
        # Loop - until both l1 and l2 empty
        while l1 or l2:
            # pop l1:
            l1_val = 0
            if l1:
                l1_val = l1.val
            
            # pop l2:
            l2_val = 0
            if l2:
                l2_val = l2.val
            
            # addition include carry and update carry
            new_val = l1_val + l2_val + carry
            carry = new_val // 10
            new_val = new_val % 10
                
            # update l1 and l2:
            if l1:
                l1.val = new_val
                l1 = l1.next
                longer_l = dummy_1
            if l2:
                l2.val = new_val
                l2 = l2.next
                longer_l = dummy_2
            
        # last carry check
        if carry == 1:
            temp_longer = longer_l # store solution pointer
            
            # loop - pointer to the last node
            while temp_longer.next:
                temp_longer = temp_longer.next
            
            # add 1
            temp_longer.next = ListNode(val=1, next=None)
        
        # RETURN
        return longer_l.next