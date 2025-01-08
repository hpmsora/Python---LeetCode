class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(_str1:str, _str2:str) -> bool:
            len_str1 = len(_str1)

            if len(_str2) < len_str1:
                return False
            if _str1 == _str2[:len_str1] and _str1 == _str2[-len_str1:]:
                print((_str1, _str2))
                return True
            else:
                return False
        sol = 0
        for index, each_words_1 in enumerate(words[:-1]):
            for each_words_2 in words[index+1:]:
                if isPrefixAndSuffix(each_words_1, each_words_2):
                    sol += 1
        return sol