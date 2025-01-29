class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for each_s in s:
            if each_s.isalnum():
                new_s += each_s.lower()
        return new_s == new_s[::-1]