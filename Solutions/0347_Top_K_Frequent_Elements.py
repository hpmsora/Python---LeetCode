class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for each_nums in nums:
            if each_nums in freq_dict:
                freq_dict[each_nums] += 1
            else:
                freq_dict[each_nums] = 1

        heap = []

        for key, value in freq_dict.items():
            heap.append((-value, key))
        
        heapq.heapify(heap)

        sol = []

        while heap and k > 0:
            _, key = heapq.heappop(heap)
            sol = [key] + sol
            k -= 1
        
        return sol