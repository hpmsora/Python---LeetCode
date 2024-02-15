class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [(float('-inf'), x) for x in range(k)]

        heapq.heapify(heap)

        for num in arr:
            diff = abs(x - num)

            last_diff, last_num = heap[0]

            last_diff *= -1

            if last_diff > diff:
                heapq.heappushpop(heap, (-1*diff, num))
        
        sol = []
        for _, val in heap:
            sol.append(val)

        return sorted(sol)
            
