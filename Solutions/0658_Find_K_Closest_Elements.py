class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        mid = 0

        while left < right:
            mid = (left + right) // 2

            if arr[mid] > x:
                right = mid
            elif x > arr[mid+k]:
                left = mid + 1
            else:
                mid_dist = abs(arr[mid] - x)
                mid_k_dist = abs(arr[mid+k] - x)

                if mid_dist <= mid_k_dist:
                    right = mid
                else:
                    left = mid + 1
        
        return arr[left:left+k]