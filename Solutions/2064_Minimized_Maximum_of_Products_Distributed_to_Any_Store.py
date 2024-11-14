class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        heap = []

        heapq.heapify(heap)
        curr_n = 0

        for each_quantities in quantities:
            heapq.heappush(heap, (each_quantities * -1, -1, each_quantities))
            curr_n += 1

        while curr_n < n:
            largest_quant, freq, total = heapq.heappop(heap)
            heapq.heappush(heap, (total/(freq*-1+1)*-1, freq-1, total))
            curr_n += 1
        return math.ceil(heapq.heappop(heap)[0]*-1)