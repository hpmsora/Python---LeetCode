class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0

        for each_s in s:
            if each_s == "1":
                right += 1
        
        sol = 0
        for each_s in s[:-1]:
            if each_s == "1":
                right -= 1
            else:
                left += 1
            sol = max(sol, right + left)
        return sol