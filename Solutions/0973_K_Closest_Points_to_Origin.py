class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Distance helper function
        def helper(_x:int , _y:int ) -> int:
            return -1*(_x**2 + _y**2)**0.5

        # Solution Variable
        sol = [(float('-inf'), 0, 0) for _ in range(k)]
        
        # Heap
        heapq.heapify(sol)

        # Loop for each point (x: int, y: int)
        for x, y in points:
            # Get largest distnace from heap
            min_val, _, _ = sol[0]

            # Get current x, y euc-distance
            dis = helper(x, y)

            # Check current position is valid
            if dis > min_val:
                heapq.heappushpop(sol, (dis, x, y))
        
        # RETURN
        return [[x, y] for _, x, y in sol]