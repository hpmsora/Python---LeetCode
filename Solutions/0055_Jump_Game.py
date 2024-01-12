class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0

        for i in range(len(nums)):

            if i>reachable:
                return False  

            reachable = max(reachable, i+nums[i])
            
        return True