class Solution:
    def removeVowels(self, s: str) -> str:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}

        sol = ''

        for letter in s:
            if not letter in vowels_set:
                sol += letter
        
        return sol