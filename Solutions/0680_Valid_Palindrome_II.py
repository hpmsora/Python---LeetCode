class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                left_skip = s[left+1:right+1]
                right_skip = s[left:right]
                return left_skip == left_skip[::-1] or right_skip == right_skip[::-1]
        return True