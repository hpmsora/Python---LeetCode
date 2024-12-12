class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left = 1
        right = max(ribbons)

        sol = 0

        while left <= right:
            mid = left + (right - left) // 2

            nums = 0

            for each_ribbons in ribbons:
                nums += each_ribbons // mid
                if nums >= k:
                    sol = max(sol, mid)
                    break

            if nums >= k:
                left = mid + 1
            else:
                right = mid - 1
        
        return sol