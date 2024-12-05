class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_freq = {}

        for each_nums in nums:
            if each_nums in count_freq:
                count_freq[each_nums] += 1
            else:
                count_freq[each_nums] = 1

        heap = [(0, -1) for _ in range(k)]

        heapq.heapify(heap)

        for num, freq in count_freq.items():
            if heap[0][0] < freq:
                heapq.heappushpop(heap, (freq, num))
        
        sol = []

        for _, num in heap:
            sol.append(num)
        return sol