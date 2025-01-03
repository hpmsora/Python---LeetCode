class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n_vowels_list = []
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        n_isVowel = 0
        for each_words in words:
            if each_words[0] in vowels and each_words[-1] in vowels:
                n_isVowel += 1
            n_vowels_list.append(n_isVowel)
        
        n_vowels_list.append(0)

        sol = []

        for start, end in queries:
            sol.append(n_vowels_list[end] - n_vowels_list[start - 1])
        return sol