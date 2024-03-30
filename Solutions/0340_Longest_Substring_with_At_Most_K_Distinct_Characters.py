class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right = 0, 0

        char_dict = {}

        sol = 0

        while right < len(s):
            char = s[right]

            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

            if len(char_dict) > k:
                while left <= right and len(char_dict) > k:
                    left_char = s[left]

                    char_dict[left_char] -= 1
                    if char_dict[left_char] == 0:
                        del char_dict[left_char]
                    
                    left += 1
            sol = max(sol, right - left + 1)

            right += 1

        return sol