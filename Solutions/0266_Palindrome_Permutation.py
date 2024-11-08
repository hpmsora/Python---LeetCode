class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        letter_count = {}

        for each_s in s:
            if each_s in letter_count:
                letter_count[each_s] += 1
            else:
                letter_count[each_s] = 1
        
        odd_count = 0
        for value in letter_count.values():
            if value % 2 == 1:
                odd_count += 1
                if odd_count > 1:
                    return False
        return True