class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]

        heapq.heapify(heap)

        for each_nums in nums[k:]:
            if each_nums > heap[0]:
                heapq.heappushpop(heap, each_nums)
        
        return heap[0]