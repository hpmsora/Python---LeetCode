class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0','1','2','3','4','5','6','7','8','9'])
        left = 0
        right = len(s) - 1
        while left < right:
            # Next Left
            while left < right and not s[left].lower() in char_list:
                left += 1
            left_letter = s[left].lower()
            left += 1

            # Next Right
            while 0 <= right and not s[right].lower() in char_list:
                right -= 1
            right_letter = s[right].lower()
            right -= 1

            if not left_letter in char_list:
                return True

            if not (left_letter == right_letter):
                return False
        return True