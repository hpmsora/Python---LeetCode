class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        nums2_dict = {}
        
        for each_nums1 in nums1:
            if each_nums1 in nums1_dict:
                nums1_dict[each_nums1] += 1
            else:
                nums1_dict[each_nums1] = 1
                
        for each_nums2 in nums2:
            if each_nums2 in nums2_dict:
                nums2_dict[each_nums2] += 1
            else:
                nums2_dict[each_nums2] = 1
                
        sol = []
        for each_num, freq in nums1_dict.items():
            if each_num in nums2_dict:
                sol += [each_num] * min(nums2_dict[each_num], freq)
        return sol