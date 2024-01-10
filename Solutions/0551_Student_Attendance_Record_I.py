class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for each_s in s:
            if each_s == 'A':
                a += 1
                if a == 2:
                    return False
                l = 0
            elif each_s == 'L':
                l += 1
                if l == 3:
                    return False
            else:
                l = 0
        return True