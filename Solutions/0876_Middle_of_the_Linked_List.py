# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Visited node save
        # key: index, val: ListNode
        visited_dict = {}

        # Index count variable
        index = 0

        # Loop - all node
        while head:
            # Update visited node dictionary
            visited_dict[index] = head

            # Update head
            head = head.next

            # Update index
            index += 1

        # Find middle index
        index = index // 2

        # RETURN - middle index head
        return visited_dict[index]