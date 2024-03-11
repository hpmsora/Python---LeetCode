# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Freqeuncy dictionary
        val_freq_dict = {}

        # Loop - all element
        while head:
            # Get value of each node
            val = head.val

            # Update freqeuncy dictionary
            if val in val_freq_dict:
                val_freq_dict[val] += 1
            else:
                val_freq_dict[val] = 1

            # Update head
            head = head.next

        # Construct new linked list
        dummy = ListNode(val = -1)
        head = dummy

        # Loop - all frequency dictionary (freq only)
        for freq in val_freq_dict.values():
            new_node = ListNode(val = freq)
            head.next = new_node
            head = new_node
        
        # RETURN - freqeuncy linked list
        return dummy.next