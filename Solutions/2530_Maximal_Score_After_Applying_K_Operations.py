class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        def newNum(_num):
            return floor(_num/3)
        
        heap = []

        for each_nums in nums:
            heapq.heappush(heap, each_nums * -1)
        
        sol = 0

        while k > 0:

            sol -= heapq.heappushpop(heap, newNum(heap[0]))

            k -= 1

        return sol