class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        heap = []
        
        heapq.heapify(heap)
        
        prev_time = 0
        
        for t, key in zip(releaseTimes, keysPressed):
            duration = t - prev_time
            
            heapq.heappush(heap, (-1 * duration, -1 * ord(key)))
            
            prev_time = t
            
        return chr(-1 * heap[0][1])