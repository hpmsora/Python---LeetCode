class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        next_letter = {
            'a' : 'b', 'b' : 'c', 'c' : 'd', 'd' : 'e', 'e' : 'f',
            'f' : 'g', 'g' : 'h', 'h' : 'i', 'i' : 'j', 'j' : 'k',
            'k' : 'l', 'l' : 'm', 'm' : 'n', 'n' : 'o', 'o' : 'p',
            'p' : 'q', 'q' : 'r', 'r' : 's', 's' : 't', 't' : 'u',
            'u' : 'v', 'v' : 'w', 'w' : 'x', 'x' : 'y', 'y' : 'z',
            'z' : 'a'
        }

        if len(str1) < len(str2):
            return False
        
        index_str2 = 0
        for each_letter in str1:
            if each_letter == str2[index_str2]:
                index_str2 += 1
            elif next_letter[each_letter] == str2[index_str2]:
                index_str2 += 1
            
            if index_str2 == len(str2):
                return True
        return False