class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_nums_dict = {}
        for index, each_nums in enumerate(nums):
            if not each_nums == 0:
                self.index_nums_dict[index] = each_nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sol = 0
        for index, each_nums in self.index_nums_dict.items():
            if index in vec.index_nums_dict:
                sol += each_nums * vec.index_nums_dict[index]
        return sol

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)