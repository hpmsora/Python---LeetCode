class Solution:
    def removeVowels(self, s: str) -> str:
        vowels_list = ['a', 'e', 'i', 'o', 'u']

        for vowel in vowels_list:
            s = s.replace(vowel, '')
        return s