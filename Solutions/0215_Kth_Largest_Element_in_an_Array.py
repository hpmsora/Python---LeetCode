class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Declare basic heap list
        heap = nums[:k]

        # Heapify
        heapq.heapify(heap)

        # Loop - rest of numbers
        for each_nums in nums[k:]:
            # Check each_nums is bigger than smallest number in heap
            if each_nums > heap[0]:
                # Update heap
                heapq.heappushpop(heap, each_nums)
        
        # RETURN - first element of heap
        return heap[0]