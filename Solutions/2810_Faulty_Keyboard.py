class Solution:
    def finalString(self, s: str) -> str:
        sol = ""

        for each_s in s:
            if each_s == "i":
                sol = sol[::-1]
            else:
                sol += each_s

        return sol