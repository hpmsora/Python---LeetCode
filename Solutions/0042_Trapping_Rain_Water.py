class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                volume += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                volume += right_max - height[right]

        return volume