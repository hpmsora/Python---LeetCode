class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        nums = [0, 1, 1]
        
        for index in range(3,n+1):
            nums.append(nums[index-3] + nums[index-2]+nums[index-1])
        return nums[-1]