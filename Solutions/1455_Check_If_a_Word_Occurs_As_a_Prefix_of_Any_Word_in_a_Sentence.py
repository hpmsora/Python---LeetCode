class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for index, each_word in enumerate(sentence.split()):
            if not len(each_word) < len(searchWord) and each_word[:len(searchWord)] == searchWord:
                return index + 1
        return -1