class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n_0 = 0 # number of zeros
        n_1 = -1 # number of ones (at least one "1")

        # Loop - iterate all number in s
        for each_s in s:
            if each_s == "0":   # Zerp
                n_0 += 1
            else:               # Ones
                n_1 += 1

        # Default solution since there is at least one "1".
        sol = "1"

        # RETURN (Front all "1" behind all "0")
        return "1"*n_1 + "0"*n_0 + sol