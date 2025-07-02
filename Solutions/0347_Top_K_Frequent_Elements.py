class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        heap = [] # [(freq, num), ...]
        heapq.heapify(heap)
        for num, freq in freq_dict.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                if heap[0][0] < freq:
                    heapq.heappushpop(heap, (freq, num))
        
        sol = []
        for _, num in heap:
            sol.append(num)
        return sol