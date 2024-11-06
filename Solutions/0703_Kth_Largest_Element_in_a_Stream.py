class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        if len(nums) < k:
            nums += [float('-inf')] * (k - len(nums))
            self.heap = nums
        else:
            self.heap = nums[:k]
        
        heapq.heapify(self.heap)
        for each_nums in nums[k:]:
            if self.heap[0] < each_nums:
                heapq.heappushpop(self.heap,each_nums)

    def add(self, val: int) -> int:
        if self.heap[0] < val:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)