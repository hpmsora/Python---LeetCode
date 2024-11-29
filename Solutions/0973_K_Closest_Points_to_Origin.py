class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # cal euc
        def helper(_x, _y):
            return (_x**2 + _y**2) * -1

        heap = []
        heapq.heapify(heap)
        for x, y in points[:k]:
            dis = helper(x, y)
            heapq.heappush(heap, (dis, x, y))

        for x, y in points[k:]:
            dis = helper(x, y)
            if heap[0][0] < dis:
                heapq.heappushpop(heap, (dis, x, y))
        
        sol = []
        for _, x, y in heap:
            sol.append([x, y])

        return sol