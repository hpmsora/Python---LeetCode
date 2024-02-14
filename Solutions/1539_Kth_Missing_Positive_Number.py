class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 0
        while k > 0:
            num += 1
            if arr:
                if arr[0] == num:
                    arr.pop(0)
                else:
                    k -= 1
            else:
                k -= 1
        return num