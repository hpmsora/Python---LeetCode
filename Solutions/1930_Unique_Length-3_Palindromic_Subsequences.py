class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        sol = 0

        for each_s in set(s):
            left_most, right_most = s.find(each_s), s.rfind(each_s)
            if left_most + 1 < right_most:
                sol += len(set(s[left_most+1:right_most]))
        return sol