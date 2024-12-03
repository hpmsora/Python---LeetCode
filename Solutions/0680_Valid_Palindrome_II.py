class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s_list = list(s)

        while left < right:
            if s_list[left] == s_list[right]:
                left += 1
                right -= 1
            else:
                return s_list[left+1:right+1] == s_list[left+1:right+1][::-1] or s_list[left:right] == s_list[left:right][::-1]
        return True