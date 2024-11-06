class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        
        vowel_set = {"a", "e", "i", "o", "u"}
        
        index = 0
        while index < len(words):
            each_words = words[index]
            first_letter = each_words[0].lower()
            if first_letter in vowel_set:
                words[index] += "ma"
            else:
                words[index] = words[index][1:] + words[index][0] + "ma"
            
            words[index] = words[index] + "a"*(index+1)
            index += 1
        return " ".join(words)