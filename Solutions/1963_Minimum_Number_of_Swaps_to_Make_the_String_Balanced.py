class Solution:
    def minSwaps(self, s: str) -> int:
        open_b = 0
        sol = 0

        for each_s in s:
            if each_s == "[":
                open_b += 1
            elif each_s == "]":
                if open_b <= 0:
                    sol += 1
                else:
                    open_b -= 1
        return (sol+1)//2