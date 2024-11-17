from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """Find the Power of K-Size Subarrays"""
        # Skip if k is 1
        if k == 1:
            return nums
            
        n = len(nums)
        result = []
        left = 0
        right = 1
        
        while right < n:
            # Check if current sequence is not consecutive
            is_not_consecutive = nums[right] - nums[right-1] != 1
            
            if is_not_consecutive:
                # Mark invalid sequences
                while left < right and left + k - 1 < n:
                    result.append(-1)
                    left += 1
                left = right
            # Found valid k-length sequence
            elif right - left == k - 1:
                result.append(nums[right])
                left += 1
                
            right += 1
            
        return result