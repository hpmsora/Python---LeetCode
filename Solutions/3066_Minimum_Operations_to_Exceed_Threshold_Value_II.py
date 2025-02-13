class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for each_nums in nums:
            if each_nums < k:
                heapq.heappush(heap, each_nums)

        sol = 0
        while heap:
            if len(heap) == 1:
                sol += 1
                return sol

            num_1 = heapq.heappop(heap)
            num_2 = heap[0]

            new_num = min(num_1, num_2) * 2 + max(num_1, num_2)

            if new_num < k:
                heapq.heappushpop(heap, new_num)
            else:
                heapq.heappop(heap)
            sol += 1
        return sol