class Solution:
    def check_p(self, _s):
        half_len_s = len(_s) // 2
        if len(_s) % 2 == 0:
            return _s[:half_len_s] == _s[half_len_s:][::-1]
        else:
            return _s[:half_len_s] == _s[half_len_s+1:][::-1]
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                if left >= right:
                    return True
            else:
                if left + 1 < right:
                    return self.check_p(s[left+1:right+1]) or self.check_p(s[left:right])
                else:
                    return True
        return True