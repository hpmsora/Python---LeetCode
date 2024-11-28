class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums_dict = {}
        
        for index, each_nums in enumerate(nums):
            if not each_nums == 0:
                self.nums_dict[index] = each_nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sol = 0
        for each_keys, value in vec.nums_dict.items():
            if each_keys in self.nums_dict:
                sol += value * self.nums_dict[each_keys]
        return sol
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)