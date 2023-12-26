class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        uset = set()

        for i in range(len(nums)):
            if not nums[i] in uset:
                nums[len(uset)] = nums[i]
                uset.add(nums[i])
                count += 1
        return count