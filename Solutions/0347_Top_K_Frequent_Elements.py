class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for each_nums in nums:
            if each_nums in freq_dict:
                freq_dict[each_nums] += 1
            else:
                freq_dict[each_nums] = 1

        heap = [(0, float('inf')) for _ in range(k)]

        heapq.heapify(heap)

        for key, freq in freq_dict.items():
            if heap[0][0] < freq:
                heapq.heappushpop(heap, (freq, key))
        sol = []

        for _, value in heap:
            sol.append(value)
        return sol