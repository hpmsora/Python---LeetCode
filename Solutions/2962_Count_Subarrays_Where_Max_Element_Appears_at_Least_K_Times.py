class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left, right = 0, 0

        max_num = max(nums)

        freq = 0
        sol = 0

        while right < len(nums):
            num = nums[right]

            if num == max_num:
                freq += 1
            
            if freq >= k:
                while left <= right and freq >= k:
                    if nums[left] == max_num:
                        freq -= 1
                    left += 1
                left -= 1
                freq += 1
                sol += left + 1
            right += 1

        return sol