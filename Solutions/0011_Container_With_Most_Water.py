class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        sol = 0

        while left < right:
            n_left = height[left]
            n_right = height[right]

            sol = max(sol, min(n_left, n_right)*(right-left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return sol 