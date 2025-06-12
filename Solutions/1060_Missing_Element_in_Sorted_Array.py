class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        prev = nums[0]
        
        for num in nums:
            gap = num - prev - 1
            prev = num
            if gap > 0:
                k -= gap
            if k <= 0:
                return num + k - 1
        
        return nums[-1] + k