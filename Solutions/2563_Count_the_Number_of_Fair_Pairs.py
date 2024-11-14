class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        left = 0
        right = len(nums)-1
        min_right = len(nums)-1

        sol = 0

        while left < right:
            # right stratch
            while right >= left and nums[left] + nums[right] > upper:
                if left == right:
                    break
                right -= 1
            
            # min_right stratct
            if min_right < left:
                min_right = left
            while nums[left] + nums[min_right] >= lower:
                if left == min_right:
                    break
                min_right -= 1
            sol += right - min_right
            left += 1
        return sol