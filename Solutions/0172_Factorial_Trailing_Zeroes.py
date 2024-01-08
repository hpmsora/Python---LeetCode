class Solution:
    def trailingZeroes(self, n: int) -> int:
        sol = 0

        while not n == 0:
            n = int(n/5)
            sol += n

        return sol