class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_freq_dict = {}
        for each_s in s:
            if each_s in char_freq_dict:
                char_freq_dict[each_s] += 1
            else:
                char_freq_dict[each_s] = 1
        odd_count = 0
        for freq in char_freq_dict.values():
            if freq % 2 == 1:
                odd_count += 1
                if odd_count > 1:
                    return False
        return True