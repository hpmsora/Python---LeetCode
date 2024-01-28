class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {
            'a',
            'e',
            'i',
            'o',
            'u',
            'A',
            'E',
            'I',
            'O',
            'U'
        }
        
        index_list = []
        char_list = []
        for index in range(len(s)):
            char = s[index]
            
            if char in vowels:
                index_list.append(index)
                char_list.append(char)
        
        s_list = list(s)
        for index, char in zip(reversed(index_list), char_list):
            s_list[index] = char
            
        s = ''.join(s_list)
            
        return s