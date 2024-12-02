# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sol = ListNode(next=None)
        head = sol

        heap = []

        for index, each_lists in enumerate(lists):
            if each_lists:
                heap.append((each_lists.val, index, 0, each_lists))
        heapq.heapify(heap)

        while heap:
            val, index_lists, index, smallest_num = heap[0]

            head.next = smallest_num
            head = head.next

            if smallest_num.next:
                heapq.heappushpop(heap, (smallest_num.next.val, index_lists, index + 1, smallest_num.next))
            else:
                heapq.heappop(heap)
        head.next = None
        return sol.next