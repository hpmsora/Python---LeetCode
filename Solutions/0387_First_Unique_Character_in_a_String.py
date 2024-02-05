class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = {}
        for each_s in s:
            if each_s in s_dict:
                s_dict[each_s] += 1
            else:
                s_dict[each_s] = 1
        
        for index in range(len(s)):
            each_s = s[index]

            if s_dict[each_s] == 1:
                return index
        return -1