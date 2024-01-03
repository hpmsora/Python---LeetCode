class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while not n == 0:
            if n & 1:
                count += 1
            n = n >> 1
        return count