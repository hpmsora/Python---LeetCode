class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol = [0, 0]

        nums1_set = set(nums1)
        nums2_set = set(nums2)

        for num in nums1:
            if num in nums2_set:
                sol[0] += 1
        for num in nums2:
            if num in nums1_set:
                sol[1] += 1

        return sol