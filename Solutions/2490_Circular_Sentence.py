class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        first_letter = words[0][0]

        last_letter = words[0][-1]
        for each_words in words[1:]:
            if not last_letter == each_words[0]:
                return False
            else:
                last_letter = each_words[-1]

        if first_letter == last_letter:
            return True
        else:
            return False