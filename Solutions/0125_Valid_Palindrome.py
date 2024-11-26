class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s_list = list(s)
        #index = 0
        #while index < len(s_list):
        #    if s_list[index].isalnum():
        #        s_list[index] = s_list[index].lower()
        #    else:
        #        s_list[index] = ""
        #    index += 1
        #return ''.join(s_list) == ''.join(s_list[::-1])

        left = 0
        right = len(s) - 1

        s_list = list(s)

        while left <= right:
            while left <= right and not s[left].isalnum():
                left += 1
            
            if left >= right:
                return True
            
            while left <= right and not s[right].isalnum():
                right -= 1

            if not s_list[left].lower() == s_list[right].lower():
                return False
            left += 1
            right -= 1
        return True