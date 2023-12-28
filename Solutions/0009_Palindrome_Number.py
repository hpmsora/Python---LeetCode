class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            return str(x) == ''.join(reversed(str(x)))
        else:
            return False