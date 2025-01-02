class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]

        heapq.heapify(heap)

        for each_nums in nums[k:]:
            if heap[0] < each_nums:
                heapq.heappushpop(heap, each_nums)
        return heap[0]