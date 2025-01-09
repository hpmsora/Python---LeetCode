class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        sol = 0
        p_len = len(pref)
        for each_words in words:
            if len(each_words) >= p_len and pref == each_words[:p_len]:
                sol += 1
        return sol