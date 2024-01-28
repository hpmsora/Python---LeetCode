class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for index in range(len(s)//2):
            if len(s) % (index + 1) == 0:
                multi = len(s) // (index + 1)
                
                if s == s[:index+1] * multi:
                    return True
        return False