class Solution:
    def compressedString(self, word: str) -> str:
        sol = ""

        prev_letter = word[0]
        dup_len = 1
        
        for each_word in word[1:]:
            if each_word == prev_letter:
                if dup_len == 9:
                    sol += str(dup_len) + prev_letter
                    dup_len = 0
                dup_len += 1
            else:
                sol += str(dup_len) + prev_letter
                prev_letter = each_word
                dup_len = 1
        
        sol += str(dup_len) + prev_letter

        return sol