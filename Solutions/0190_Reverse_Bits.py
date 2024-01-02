class Solution:
    def reverseBits(self, n: int) -> int:
        def helper(n, sol, count):
            if n < 1:
                return sol<<(32-count)
            return helper(n>>1, (sol<<1)|(n&1), count+1)
        return helper(n, 0, 0)