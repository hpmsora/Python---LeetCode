class Solution:
    def longestPalindrome(self, s: str) -> str:
        sol = ""
        max_len = 0

        # odd
        index = 0

        while index < len(s):
            left = index - 1
            right = index + 1
            while left >= 0 and right < len(s):
                if not s[left] == s[right]:
                    diff = right - left - 1
                    if diff > max_len:
                        sol = s[left + 1:right]
                        max_len = diff
                    break
                else:
                    left -= 1
                    right += 1
            diff = right - left - 1
            if diff > max_len:
                sol = s[left + 1:right]
                max_len = diff
            index += 1

        # even
        index = 0

        while index < len(s):
            left = index
            right = index + 1
            while left >= 0 and right < len(s):
                if not s[left] == s[right]:
                    diff = right - left - 1
                    if diff > max_len:
                        sol = s[left + 1:right]
                        max_len = diff
                    break
                else:
                    left -= 1
                    right += 1
            diff = right - left - 1
            if diff > max_len:
                sol = s[left + 1:right]
                max_len = diff
            index += 1
        return sol