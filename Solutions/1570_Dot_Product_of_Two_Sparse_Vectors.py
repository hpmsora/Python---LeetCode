class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sol = 0
        for num1, num2 in zip(self.nums, vec.nums):
            if (not num1 == 0) and (not num2 == 0):
                sol += num1 * num2
        return sol

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)