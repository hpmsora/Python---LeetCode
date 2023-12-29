class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}

        for index, num in enumerate(nums):
            if num in nums_dict and index - nums_dict[num] <= k:
                return True
            else:
                nums_dict[num] = index
        return False