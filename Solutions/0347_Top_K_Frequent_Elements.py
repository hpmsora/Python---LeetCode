class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        for each_nums in nums:
            if each_nums in nums_dict:
                nums_dict[each_nums] += 1
            else:
                nums_dict[each_nums] = 1

        heap = [(0, 0)] # (Freq, Key)
        heapq.heapify(heap)

        for key, value in nums_dict.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            elif heap[0][0] < value:
                heapq.heappushpop(heap, (value, key))
        
        sol = []
        for _, each_heap in heap:
            sol.append(each_heap)
        return sol