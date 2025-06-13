class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = {}
        def dfs(index_1, index_2):
            if index_1 == len(nums1) or index_2 == len(nums2):
                return 0
            elif (index_1, index_2) in dp:
                return dp[(index_1, index_2)]
            
            if nums1[index_1] == nums2[index_2]:
                return 1 + dfs(index_1 + 1, index_2 + 1)
            else:
                dp[(index_1, index_2)] = max(dfs(index_1 + 1, index_2), dfs(index_1, index_2 + 1))
            return dp[(index_1, index_2)]
        return dfs(0, 0)