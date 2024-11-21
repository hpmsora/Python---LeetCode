class Solution:
    def validPalindrome(self, s: str) -> bool:
        right = len(s)-1
        left = 0
        if s == s[::-1]:
            return True
        else:
            while(s[left]==s[right]):
                left += 1
                right -= 1
            
            return s[left+1:right+1] == s[left+1:right+1][::-1] or s[left:right] == s[left:right][::-1]