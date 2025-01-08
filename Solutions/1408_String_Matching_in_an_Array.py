class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sol = []

        for index_1, each_words in enumerate(words):
            for index_2, each_words_2 in enumerate(words):
                if each_words in each_words_2 and not index_1 == index_2:
                    sol.append(each_words)
                    break
        return sol