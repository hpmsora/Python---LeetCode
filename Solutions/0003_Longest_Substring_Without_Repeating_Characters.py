class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def remove_letter_from_dict(_freq_dict, _letter):
            if _letter in _freq_dict:
                if _freq_dict[_letter] == 1:
                    del _freq_dict[_letter]
                else:
                    _freq_dict[_letter] -= 1
            else:
                _freq_dict[_letter] = 1

        left = 0
        freq_dict = {}
        sol = 0

        for index, letter in enumerate(s):
            if letter in freq_dict:
                freq_dict[letter] += 1
            else:
                freq_dict[letter] = 1

            while not (len(freq_dict) == index - left + 1) and index >= left:
                left_letter = s[left]
                remove_letter_from_dict(freq_dict, left_letter)
                left += 1

            sol = max(sol, index - left + 1)
        return sol