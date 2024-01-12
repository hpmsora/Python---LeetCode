class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = 0, 0
        vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_size = len(s)
        limit = int(s_size/2)

        for index in range(s_size):
            if s[index] in vowels_set:
                if index <= limit - 1:
                    a += 1
                else:
                    b += 1
        return a == b