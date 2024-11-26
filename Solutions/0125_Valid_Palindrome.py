class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = list(s)

        index = 0
        while index < len(s_list):
            if s_list[index].isalnum():
                s_list[index] = s_list[index].lower()
            else:
                s_list[index] = ""
            index += 1

        return ''.join(s_list) == ''.join(s_list[::-1])