class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        alphabet_set = {
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        }
        alphabet_upper_set = {
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        }
        numerical_set = {
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
        }
        while left < right:
            # Left Stratch
            while left < right and not (s[left] in alphabet_set or s[left] in alphabet_upper_set or s[left] in numerical_set):
                left += 1
            
            if left == right:
                return True
            
            # Right Stratch
            while left < right and not (s[right] in alphabet_set or s[right] in alphabet_upper_set or s[right] in numerical_set):
                right -= 1
            if left == right:
                return True
            
            if not s[left].lower() == s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True