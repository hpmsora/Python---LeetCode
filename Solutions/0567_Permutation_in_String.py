class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        
        for each_s1 in s1:
            if each_s1 in s1_dict:
                s1_dict[each_s1] += 1
            else:
                s1_dict[each_s1] = 1
        
        if len(s1) > len(s2):
            return False
        
        left = 0
        right = 0
        len_s1 = len(s1)
        curr_dict = {}
        
        while right < len(s2):
            curr_letter = s2[right]
            if curr_letter in curr_dict:
                curr_dict[curr_letter] += 1
            else:
                curr_dict[curr_letter] = 1
                
            if curr_letter in s1_dict:
                while right-left + 1 > len_s1:
                    left_letter = s2[left]
                    
                    if curr_dict[left_letter] == 1:
                        del curr_dict[left_letter]
                    else:
                        curr_dict[left_letter] -= 1
                    
                    left += 1
                if right-left + 1 == len_s1:
                    isSol = True
                    for letter, freq in curr_dict.items():
                        if not s1_dict[letter] == freq:
                            isSol = False
                    if isSol:
                        return True
            else:
                left = right + 1
                curr_dict = {}
            right += 1
        return False