class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
            sum_indices = {0: -1}  # Initialize with sum 0 at index -1
            max_length = 0
            cumulative_sum = 0

            # Iterate over the array
            for i, num in enumerate(nums):
                cumulative_sum += num  # Add the current number to the cumulative sum
                
                # If (cumulative_sum - k) is in the dictionary, we found a subarray that sums to k
                if (cumulative_sum - k) in sum_indices:
                    max_length = max(max_length, i - sum_indices[cumulative_sum - k])

                # If this cumulative sum is not in the dictionary, add it with the current index
                if cumulative_sum not in sum_indices:
                    sum_indices[cumulative_sum] = i

            return max_length