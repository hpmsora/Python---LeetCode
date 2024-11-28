class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums_dict = {}
        
        for index, each_nums in enumerate(nums):
            if not each_nums == 0:
                self.nums_dict[index] = each_nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sol = 0
        val_1 = self.nums_dict
        val_2 = vec.nums_dict
        if len(self.nums_dict) > len(vec.nums_dict):
            val_1 = vec.nums_dict
            val_2 = self.nums_dict
        for each_keys, value in val_1.items():
            if each_keys in val_2:
                sol += value * val_2[each_keys]
        return sol
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)