class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Get k length heap list
        heap = nums[:k]

        # Heapify
        heapq.heapify(heap)

        # Loop - all num in nums
        for each_nums in nums[k:]:
            # Check only valid for list
            if heap[0] < each_nums:
                # Remove smallest and add current number
                heapq.heappushpop(heap, each_nums)
                
        # RETURN
        return heap[0]