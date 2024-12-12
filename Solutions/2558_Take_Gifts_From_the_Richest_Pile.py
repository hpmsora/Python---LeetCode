class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []

        heapq.heapify(heap)

        for each_gifts in gifts:
            heapq.heappush(heap, -1 * each_gifts)

        for _ in range(k):
            heapq.heappushpop(heap, int(math.sqrt(heap[0] * -1)) * -1)

        return sum(heap) * -1