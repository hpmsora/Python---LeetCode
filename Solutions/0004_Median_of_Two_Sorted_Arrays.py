class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index_1 = 0
        index_2 = 0

        med_indices = []
        med_indices_set = set()

        if (len(nums1) + len(nums2)) % 2 == 0:
            med_indices = [(len(nums1) + len(nums2)) // 2 - 1, (len(nums1) + len(nums2)) // 2]
            med_indices_set.add((len(nums1) + len(nums2)) // 2 - 1)
            med_indices_set.add((len(nums1) + len(nums2)) // 2)
        else:
            med_indices = [(len(nums1) + len(nums2)) // 2]
            med_indices_set.add((len(nums1) + len(nums2)) // 2)

        sol = []
        if (not nums1) and (not nums2):
            return []
        elif not nums1:
            for each_med_indices in med_indices:
                sol.append(nums2[each_med_indices])
            return sum(sol)/len(sol)
        elif not nums2:
            for each_med_indices in med_indices:
                sol.append(nums1[each_med_indices])
            return sum(sol)/len(sol)
        while index_1 + index_2 <= med_indices[-1]:
            if nums1[index_1] >= nums2[index_2]:
                if index_1 + index_2 in med_indices_set:
                    sol.append(nums2[index_2])
                    if len(sol) == len(med_indices_set):
                        break
                index_2 += 1
                if not index_2 < len(nums2):
                    for each_med_index in med_indices_set:
                        if each_med_index >= index_1 + index_2:
                            sol.append(nums1[each_med_index - len(nums2)])
                    break
            else:
                if index_1 + index_2 in med_indices_set:
                    sol.append(nums1[index_1])
                    if len(sol) == len(med_indices_set):
                        break
                index_1 += 1
                if not index_1 < len(nums1):
                    for each_med_index in med_indices_set:
                        if each_med_index >= index_1 + index_2:
                            sol.append(nums2[each_med_index - len(nums1)])
                    break
        
        return sum(sol)/len(sol)