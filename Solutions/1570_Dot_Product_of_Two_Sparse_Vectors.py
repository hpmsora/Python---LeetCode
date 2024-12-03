class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums_nonzero_dict = {}
        
        for index, each_nums in enumerate(nums):
            if not each_nums == 0:
                self.nums_nonzero_dict[index] = each_nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        iter_dict = self.nums_nonzero_dict
        target_dict = vec.nums_nonzero_dict
        if len(vec.nums_nonzero_dict) < len(self.nums_nonzero_dict):
            iter_dict = vec.nums_nonzero_dict
            target_dict = self.nums_nonzero_dict
        
        sol = 0
        for key, value in iter_dict.items():
            if key in target_dict:
                sol += value * target_dict[key]
        return sol
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)