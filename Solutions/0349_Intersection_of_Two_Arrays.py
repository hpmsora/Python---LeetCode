class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_set = set(nums2)
        
        nums1_set = set(nums1)
        
        sol = []
        for each_nums1_set in nums1_set:
            if each_nums1_set in nums2_set:
                sol.append(each_nums1_set)
        return sol