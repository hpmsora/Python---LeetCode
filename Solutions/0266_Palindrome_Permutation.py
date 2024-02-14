class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s_dict = {}

        for each_s in s:
            if each_s in s_dict:
                s_dict[each_s] += 1
            else:
                s_dict[each_s] = 1

        odd_count = 0
        for _, val in s_dict.items():
            if val % 2 == 1:
                odd_count += 1
                if odd_count > 1:
                    return False
        return True