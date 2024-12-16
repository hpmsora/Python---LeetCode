class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []

        for index, each_nums in enumerate(nums):
            heap.append((each_nums, index))

        sol = [0 for _ in range(index+1)]

        heapq.heapify(heap)

        for _ in range(k):
            each_nums, index = heap[0]

            heapq.heapreplace(heap, (each_nums * multiplier, index))

        for each_nums, index in heap:
            sol[index] = each_nums
        
        return sol