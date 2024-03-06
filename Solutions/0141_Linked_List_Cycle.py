# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Visited node save variable
        visited = {}

        # Initialize pos
        pos = -1

        # Index count variable
        index = 0

        # Loop - all node
        while head:
            if head in visited: # visited node
                # Update pos
                pos = visited[head]

                # RETURN - loop exist
                return True

            else: # not visited node
                visited[head] = index

            # Update index
            index += 1

            # Update head
            head = head.next
        
        # RETURN - loop not exist
        return False