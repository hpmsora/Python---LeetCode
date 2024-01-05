class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for each_n in range(1, n + 1):
            if n % each_n == 0:
                k -= 1
                if k == 0:
                    return each_n
        return -1