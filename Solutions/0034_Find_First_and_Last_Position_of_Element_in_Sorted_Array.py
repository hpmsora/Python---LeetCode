class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                right = mid + 1
                left = mid - 1
                while left >= 0:
                    if not nums[left] == target:
                        break
                    left -= 1
                while right < len(nums):
                    if not nums[right] == target:
                        break
                    right += 1
                return [left+1, right-1]
            else:
                left = mid + 1

        return [-1, -1]