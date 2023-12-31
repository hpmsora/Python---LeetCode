class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        words_dict = {}

        for word in words:
            for letter in word:
                if letter in words_dict:
                    words_dict[letter] += 1
                else:
                    words_dict[letter] = 1
        
        n = len(words)
        for _, item in words_dict.items():
            if not item % n == 0:
                return False
        return True