class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        letter_freq_dict = {}

        for each_s in s:
            if each_s in letter_freq_dict:
                letter_freq_dict[each_s] += 1
            else:
                letter_freq_dict[each_s] = 1

        odd_count = 0

        for freq in letter_freq_dict.values():
            if freq % 2 == 1:
                odd_count += 1
                if odd_count > 1:
                    return False
        return True