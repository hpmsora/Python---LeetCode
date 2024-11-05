class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums)

        if len(nums_set) < 3:
            return max(nums_set)

        nums_list = list(nums_set)
        heap = nums_list[:3]
        heapq.heapify(heap)

        for each_nums_set in nums_list[3:]:
            if heap[0] < each_nums_set:
                heapq.heappushpop(heap, each_nums_set)
        
        return heap[0]