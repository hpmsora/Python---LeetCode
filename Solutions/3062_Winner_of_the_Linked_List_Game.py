# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        # Winning count
        # sol > 0: Even win
        # sol == 0: Tie
        # sol < 0: Odd win
        sol = 0

        # Loop variable
        index = 1

        # First value
        pre_num = head.val
        head = head.next

        # Loop - all value access
        while head:
            if index % 2 == 0: # index even
                pre_num = head.val
            else: # index odd
                if pre_num > head.val: # even win
                    sol += 1
                elif pre_num < head.val: # off win
                    sol -= 1
            
            # head update
            head = head.next

            # index update
            index += 1

        # RETURN - Winner check
        if sol > 0: # Even win
            return "Even"
        elif sol < 0: # Odd win
            return "Odd"
        else: # Tie
            return "Tie"