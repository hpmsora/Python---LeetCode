class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict = {}

        if not len(s) == len(t):
            return False

        for letter_s, letter_t in zip(s, t):
            if letter_s in anagram_dict:
                anagram_dict[letter_s] += 1
            else:
                anagram_dict[letter_s] = 1
            if letter_t in anagram_dict:
                anagram_dict[letter_t] -= 1
            else:
                anagram_dict[letter_t] = -1
        
        for value in anagram_dict.values():
            if not value == 0:
                return False
        return True