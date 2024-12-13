class Solution:
    def findScore(self, nums: List[int]) -> int:
        index_heap = []

        for index, each_nums in enumerate(nums):
            index_heap.append((each_nums, index))
        
        heapq.heapify(index_heap)

        index_set = set()
        sol = 0

        while index_heap:
            num, index = heapq.heappop(index_heap)

            if index in index_set:
                continue
            
            index_set.add(index)
            index_set.add(index - 1)
            index_set.add(index + 1)

            sol += num
        
        return sol