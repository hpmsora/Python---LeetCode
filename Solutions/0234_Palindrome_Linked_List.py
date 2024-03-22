# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_node = []

        while head:
            list_node.append(head.val)
            head = head.next

        index = 0

        while index < len(list_node)//2:
            if not list_node[index] == list_node[len(list_node) - index - 1]:
                return False
            index += 1
        return True