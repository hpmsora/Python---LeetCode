class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                left = mid
                right = mid
                while left >= 0:
                    if nums[left] == target:
                        left -= 1
                    else:
                        break
                while right < len(nums):
                    if nums[right] == target:
                        right += 1
                    else:
                        break
                return [left + 1, right - 1]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]