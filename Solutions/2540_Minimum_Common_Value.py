class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_set = set(nums2)

        for num in nums1:
            if num in nums2_set:
                return num
        return -1