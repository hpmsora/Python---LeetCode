class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        sol = 0

        right = 0
        nums = [0] + nums
        for index in range(len(nums)):
            num = nums[index]
            if num == 0:
                k += 1
            while right < len(nums):
                if nums[right] == 1:
                    pass
                else:
                    if k == 0:
                        break
                    k -= 1
                right += 1
            sol = max(sol, right - index-1)
            index += 1
        return sol